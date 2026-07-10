from pathlib import Path
import os
import requests

# =========================
# INPUTS (GitHub Action)
# =========================
MODEL = os.environ["DIACRITICS_MODEL"]
API = os.environ["DIACRITICS_API"]
FILE_DEFAULT = os.environ.get("FILE_DEFAULT") or "*.md"

selected = os.environ.get("FILE", "").strip()

def restore_file(path: Path):
    print(f"I am repairing: {path}")

    text = path.read_text(encoding="utf-8")

    response = requests.post(
        API,
        data={
            "data": text,
            "model": MODEL
        }
    )

    response.raise_for_status()

    result = response.json()["result"]

    path.write_text(
        result,
        encoding="utf-8"
    )

    print(f"Hotovo: {path}")


if selected:
    files = [Path(selected)]
else:
    files = list(Path(".").rglob(FILE_DEFAULT))


for file in files:
    if file.is_file():
        restore_file(file)
