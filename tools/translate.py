from pathlib import Path
import os
import requests


# ====================================================================================================================================
# CONFIG
# Translation source and destination
#
# (cs)
# Zdrojový a cílový soubor překladu
# ====================================================================================================================================

SOURCE_FILE = Path(os.environ.get("TRANSLATE_SOURCE", "README.cs.md"))
OUTPUT_FILE = Path(os.environ.get("TRANSLATE_OUTPUT", "README.md"))

API = os.environ["TRANSLATE_API"]
MODEL = os.environ["TRANSLATE_MODEL"]


# ====================================================================================================================================
# CHECK FILE
#
# (cs)
# Kontrola existence souboru
# ====================================================================================================================================

if not SOURCE_FILE.exists():
    print(f"No translation source found: {SOURCE_FILE}")
    exit(0)


print(f"Translating: {SOURCE_FILE}")


text = SOURCE_FILE.read_text(
    encoding="utf-8"
)


# ====================================================================================================================================
# TRANSLATION REQUEST
#
# (cs)
# Požadavek na překlad
# ====================================================================================================================================

response = requests.post(
    API,
    data={
        "data": text,
        "model": MODEL
    },
    timeout=120
)

response.raise_for_status()


result = response.json()["result"]


# ====================================================================================================================================
# SAVE RESULT
#
# (cs)
# Uložení výsledku
# ====================================================================================================================================

OUTPUT_FILE.write_text(
    result,
    encoding="utf-8"
)


print(f"Done: {OUTPUT_FILE}")