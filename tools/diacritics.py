from pathlib import Path
import os
import requests


MODEL = os.environ["DIACRITICS_MODEL"]
API = os.environ["DIACRITICS_API"]

selected = os.environ.get("FILE", "").strip()


def restore_file(path: Path):
    print(f"Opravuji: {path}")

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
    files = list(Path(".").rglob("*.md"))


for file in files:
    if file.exists():
        restore_file(file)