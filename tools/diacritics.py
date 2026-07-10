from pathlib import Path
import os
import requests

# =========================
# INPUTS (GitHub Action)
# =========================
API = os.environ["DIACRITICS_API"]
FILE_DEFAULT = os.environ.get("FILE_DEFAULT", "").strip()
MODEL = os.environ["DIACRITICS_MODEL"]

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

    response = requests.post(
        API,
        data={
            "data": text,
            "model": MODEL
        },
        timeout=60
    )

    response.raise_for_status()

    result = response.json()["result"]

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


changed_files = get_changed_files()


if FILE_DEFAULT:
    # Pouze vybraný soubor, ale jen pokud byl změněn
    files = [
        Path(FILE_DEFAULT)
    ] if Path(FILE_DEFAULT) in changed_files else []

else:
    # Všechny změněné markdown soubory
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
