// Voice research panel: frontend.
// Protocol: server -> {type:'segment', role, voice, kind, text, meta, audio_bytes} then a binary
// WAV frame (when audio_bytes > 0); interleaved with {type:'question'|'transcript'|'status'|'done'|'error'}.

const $ = (s) => document.querySelector(s);
const statusEl = $('#status'), timerEl = $('#timer'), tree = $('#tree');
const qInput = $('#question'), goBtn = $('#go'), pttBtn = $('#ptt'), finalEl = $('#final');

let ws = null, pendingMeta = null, queue = [], playing = false;
let timer = null, runStart = null;

const ROLE = {
  system:     { label: '',           cls: 'status' },
  planner:    { label: 'Planner',    cls: 'planner' },
  researcher: { label: 'Researcher', cls: 'researcher' },
  aggregator: { label: 'Aggregator', cls: 'aggregator' },
  critic:     { label: 'Critic',     cls: 'critic' },
  judge:      { label: 'Judge',      cls: 'judge' },
};

function setStatus(t, ok = false) { statusEl.innerHTML = ok ? `<span style="color:var(--slate)">&#9679;</span> ${t}` : t; }
function startTimer() {
  runStart = Date.now();
  timer = setInterval(() => {
    const s = Math.floor((Date.now() - runStart) / 1000);
    timerEl.textContent = `${String((s / 60) | 0).padStart(2, '0')}:${String(s % 60).padStart(2, '0')}`;
  }, 250);
}
function stopTimer() { if (timer) clearInterval(timer); timer = null; }
function busy(on) { goBtn.disabled = on; pttBtn.disabled = on; }
function reset() { tree.innerHTML = ''; finalEl.className = 'hidden'; queue = []; pendingMeta = null; }

// ---- WebSocket --------------------------------------------------------------
function openWS() {
  return new Promise((resolve, reject) => {
    const proto = location.protocol === 'https:' ? 'wss' : 'ws';
    const sock = new WebSocket(`${proto}://${location.host}/ws`);
    sock.binaryType = 'arraybuffer';
    sock.onopen = () => resolve(sock);
    sock.onerror = reject;
    sock.onmessage = handleMessage;
    sock.onclose = () => { stopTimer(); busy(false); };
  });
}

function handleMessage(ev) {
  if (typeof ev.data === 'string') {
    const m = JSON.parse(ev.data);
    if (m.type === 'segment') {
      if (m.audio_bytes > 0) { pendingMeta = m; }          // spoken: wait for its WAV frame
      else { queue.push({ meta: m, blob: null }); if (!playing) playNext(); }  // text only: visible, no audio
    }
    else if (m.type === 'question') { setStatus(`Researching: "${m.text}"`, true); }
    else if (m.type === 'transcript') { qInput.value = m.text; setStatus(`Heard: "${m.text}"`); }
    else if (m.type === 'status') { setStatus(`${m.stage}...`); }
    else if (m.type === 'done') { showFinal(m); setStatus(`Done. ${m.rounds} critique round(s).`, true); stopTimer(); busy(false); }
    else if (m.type === 'error') { setStatus(`Error: ${m.message}`); stopTimer(); busy(false); }
  } else {
    const meta = pendingMeta; pendingMeta = null;
    if (!meta) return;
    queue.push({ meta, blob: new Blob([ev.data], { type: 'audio/wav' }) });
    if (!playing) playNext();
  }
}

// ---- Card creation ----------------------------------------------------------
function makeCard(meta) {
  const info = ROLE[meta.role] || ROLE.system;
  const isStatus = meta.kind === 'status';
  const rid = meta.meta && typeof meta.meta.rid === 'number' ? ` ${meta.meta.rid + 1}` : '';
  const card = document.createElement('div');
  card.className = `card ${info.cls}${isStatus ? ' status' : ''}`;
  const label = info.label ? `${info.label}${rid}` : '';
  const angle = meta.role === 'researcher' && meta.meta && meta.meta.angle
    ? `<div class="angle">${meta.meta.angle}</div>` : '';
  const voice = meta.voice ? `<span class="voice">${meta.voice}</span>` : '';
  card.innerHTML =
    (label ? `<div class="who">${label} ${voice}</div>` : '') +
    angle + `<div class="bubble"></div>`;
  tree.appendChild(card);
  return card;
}

// A tool call (search / fetch): a compact, unspoken chip so it is visible
// what each researcher is doing.
function renderTool(meta) {
  const rid = meta.meta && typeof meta.meta.rid === 'number' ? ` (researcher ${meta.meta.rid + 1})` : '';
  const chip = document.createElement('div');
  chip.className = 'toolcall';
  chip.textContent = `${meta.text}${rid}`;
  tree.appendChild(chip);
  chip.scrollIntoView({ behavior: 'smooth', block: 'end' });
}

// ---- Sequential playback with synced text reveal ----------------------------
async function playNext() {
  if (queue.length === 0) { playing = false; return; }
  playing = true;
  const { meta, blob } = queue.shift();

  if (meta.kind === 'tool') {              // tool call: surface it, do not speak it
    renderTool(meta);
    setTimeout(playNext, 450);            // brief beat so it is readable, then continue in order
    return;
  }

  document.querySelectorAll('.card.active').forEach(c => { c.classList.remove('active'); c.classList.add('done'); });
  const card = makeCard(meta);
  card.classList.add('active');
  card.scrollIntoView({ behavior: 'smooth', block: 'end' });
  const bubble = card.querySelector('.bubble');

  if (blob === null) {                    // no audio (TTS not reachable): show the text and move on
    bubble.textContent = meta.text || '';
    setTimeout(playNext, 900);
    return;
  }

  const url = URL.createObjectURL(blob);
  const audio = new Audio(url);
  await new Promise(r => { if (audio.readyState >= 1 && isFinite(audio.duration)) r(); else { audio.onloadedmetadata = r; audio.onerror = r; } });

  const words = (meta.text || '').split(/\s+/).filter(Boolean);
  const dur = isFinite(audio.duration) && audio.duration > 0 ? audio.duration : Math.max(1, words.length / 3);
  let iv = null;
  const reveal = () => {
    const t0 = performance.now();
    iv = setInterval(() => {
      const f = Math.min(1, (performance.now() - t0) / 1000 / dur);
      bubble.textContent = words.slice(0, Math.max(1, Math.floor(f * words.length))).join(' ');
      if (f >= 1) { clearInterval(iv); iv = null; }
    }, 55);
  };
  await new Promise(r => { audio.onplay = reveal; audio.onended = r; audio.onerror = r; audio.play().catch(r); });
  if (iv) clearInterval(iv);
  bubble.textContent = meta.text || '';
  URL.revokeObjectURL(url);
  playNext();
}

function showFinal(m) {
  finalEl.className = '';
  finalEl.innerHTML = `<h2>Answer</h2><div class="body">${(m.final || '').replace(/</g, '&lt;')}</div>`;
  finalEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// ---- Entry: typed ------------------------------------------------------------
async function ask(question) {
  reset(); busy(true); setStatus('Connecting...');
  try { ws = await openWS(); startTimer(); ws.send(JSON.stringify({ type: 'question', text: question })); }
  catch (e) { setStatus(`Connection failed: ${e}`); busy(false); }
}
goBtn.onclick = () => { const q = qInput.value.trim(); if (q) ask(q); };
qInput.addEventListener('keydown', (e) => { if (e.key === 'Enter' && qInput.value.trim()) ask(qInput.value.trim()); });

// ---- Entry: push-to-talk -----------------------------------------------------
let rec = null, chunks = [];
async function startRec() {
  if (!navigator.mediaDevices) { setStatus('Microphone unavailable.'); return; }
  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  const mime = MediaRecorder.isTypeSupported('audio/webm;codecs=opus') ? 'audio/webm;codecs=opus'
    : (MediaRecorder.isTypeSupported('audio/webm') ? 'audio/webm' : '');
  rec = new MediaRecorder(stream, mime ? { mimeType: mime } : undefined);
  chunks = [];
  rec.ondataavailable = (e) => { if (e.data.size) chunks.push(e.data); };
  rec.onstop = async () => {
    stream.getTracks().forEach(t => t.stop());
    const blob = new Blob(chunks, { type: rec.mimeType || 'audio/webm' });
    reset(); busy(true); setStatus(`Sending ${(blob.size / 1024).toFixed(0)} KB...`);
    try { ws = await openWS(); startTimer(); ws.send(await blob.arrayBuffer()); }
    catch (e) { setStatus(`Connection failed: ${e}`); busy(false); }
  };
  rec.start(); pttBtn.classList.add('recording'); setStatus('Recording. Release to send.');
}
function stopRec() { if (rec && rec.state === 'recording') { rec.stop(); pttBtn.classList.remove('recording'); } }
pttBtn.addEventListener('mousedown', startRec);
pttBtn.addEventListener('mouseup', stopRec);
pttBtn.addEventListener('mouseleave', stopRec);
pttBtn.addEventListener('touchstart', (e) => { e.preventDefault(); startRec(); });
pttBtn.addEventListener('touchend', (e) => { e.preventDefault(); stopRec(); });
