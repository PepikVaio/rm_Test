from pathlib import Path
import os
import subprocess
import requests
import re

# =========================
# INPUTS (GitHub Action)
# =========================
API = os.environ["DIACRITICS_API"]
FILE_DEFAULT = os.environ.get("FILE_DEFAULT", "").strip()
MODEL = os.environ["DIACRITICS_MODEL"]


protected = {}


def protect_markdown(text):
    global protected

    patterns = [
        r"(?m)^>\s*\[![A-Z]+\].*$",  # GitHub alerts
        r"(?m)^\[!.*$",              # badges
        r"<[^>]+>",                   # HTML tagy <br>
    ]



    counter = 0

    for pattern in patterns:
        matches = re.findall(
            pattern,
            text
        )

        for match in matches:
            key = f"MARKDOWN_PLACEHOLDER_{counter}"

            protected[key] = match

            text = text.replace(
                match,
                key
            )

            counter += 1

    return text


def restore_markdown(text):

    for key, value in protected.items():
        text = text.replace(
            key,
            value
        )

    return text


# ======================================================================================
# ADD DIACRITICS IN FILE
# Sends file content to Korektor API and replaces original content with corrected text.
#
# (cs)
# Odešle obsah souboru do Korektor API a nahradí původní obsah opraveným textem.
# ======================================================================================
def restore_file(path: Path):
    print(f"I am repairing: {path}")

    text = path.read_text(encoding="utf-8")
    original = protect_markdown(text)

    response = requests.post(
        API,
        data={
            "data": original,
            "model": MODEL
        },
        timeout=60
    )

    response.raise_for_status()

    result = response.json()["result"]
    result = restore_markdown(result)

    path.write_text(
        result,
        encoding="utf-8"
    )

    print(f"Done: {path}")

# =======================================================================================
# GET FILES CHANGED IN CURRENT PUSH
# Uses git history to find only files modified between previous and current commit.
#
# (cs)
# Pomocí historie Git zjistí pouze soubory změněné mezi předchozím a aktuálním commitem.
# =======================================================================================
def get_changed_files():
    result = subprocess.check_output(
        [
            "git",
            "diff",
            "--name-only",
            "HEAD^",
            "HEAD"
        ],
        text=True
    )

    return [
        Path(file)
        for file in result.splitlines()
    ]

# ===============================================
# FILE SELECTION LOGIC (priority)
# 1. FILE_DEFAULT defined:
#    - process only this file
#    - only if it was changed
# 2. FILE_DEFAULT empty:
#    - process all changed Markdown files
#
# (cs)
# 1. FILE_DEFAULT vyplněné:
#    - zpracuje pouze tento soubor
#    - pouze pokud byl změněn
# 2. FILE_DEFAULT prázdné:
#    - zpracuje všechny změněné Markdown soubory
# ===============================================
changed_files = get_changed_files()

if FILE_DEFAULT:
    files = [
        Path(FILE_DEFAULT)
    ] if Path(FILE_DEFAULT) in changed_files else []

else:
    files = [
        file
        for file in changed_files
        if file.suffix == ".md"
    ]

if not files:
    print("No files to repair")
    exit(0)

for file in files:
    if file.is_file():
        restore_file(file)
