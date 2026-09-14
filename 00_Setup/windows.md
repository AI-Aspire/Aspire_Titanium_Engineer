# Windows

Use Git Bash (installed with git) or WSL 2 with Ubuntu. Every command in the
READMEs is written for a POSIX shell.

## Managed laptops

If your company blocks direct downloads, ask IT for these before the first
morning: `pypi.org`, `files.pythonhosted.org`, `github.com`, `astral.sh`, and
the chat model endpoint your instructor names.

## Long paths

Enable long paths once, in an administrator PowerShell:

```powershell
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
```

## The console cannot print check marks

The scripts force UTF-8 on their own output. If you still see an encoding
error, run `chcp 65001` in the console first.
