"""Compare a JSON prompt request with the original schema-enforced API call."""
import argparse
import contextlib
import hashlib
import json
import sys
from datetime import datetime, timezone
from typing import Literal

from pydantic import BaseModel, ValidationError

from helpers import workspace as ws
from helpers.config import LLM_MODEL, require
from helpers.llm import client


class ProductBrief(BaseModel):
    product_name: str
    problem: str
    users: list[str]
    must_do: list[str]
    must_not_do: list[str]
    risk_level: Literal['low', 'medium', 'high']


def compare(text):
    """Same input and requested fields; only the strong call enforces the schema."""
    api = client()
    messages = [{'role': 'system', 'content': 'Extract a product brief from the charter. Return only JSON matching this schema:\n' + json.dumps(ProductBrief.model_json_schema())},
                {'role': 'user', 'content': text}]
    loose = api.chat.completions.create(model=LLM_MODEL, messages=messages)
    raw = loose.choices[0].message.content or ''
    try:
        ProductBrief.model_validate_json(raw)
        valid, error = True, None
    except ValidationError as exc:
        valid, error = False, str(exc)
    strict = api.chat.completions.parse(model=LLM_MODEL, messages=messages, response_format=ProductBrief)
    message = strict.choices[0].message
    return {'schema': ProductBrief.model_json_schema(), 'messages': messages,
            'requested': {'response': raw, 'validates': valid, 'validation_error': error,
                          'response_id': loose.id, 'model': loose.model},
            'enforced': {'response': message.parsed.model_dump() if message.parsed else None,
                         'refusal': message.refusal, 'finish_reason': strict.choices[0].finish_reason,
                         'response_id': strict.id, 'model': strict.model}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['compare'])
    parser.add_argument('--text', help='Same teaching text used in the interactive examples; defaults to the active charter')
    args = parser.parse_args()
    with contextlib.redirect_stdout(sys.stderr):
        require('OPENAI_API_KEY')
        text = args.text if args.text is not None else ws.load('charter')
        result = compare(text)
        result['provenance'] = {'recorded_at': datetime.now(timezone.utc).isoformat(), 'model': LLM_MODEL,
                                'input_source': 'provided text' if args.text is not None else ws.source('charter'),
                                'input_sha256': hashlib.sha256(text.encode()).hexdigest()}
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
