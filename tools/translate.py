from pathlib import Path
import os
import requests


# ====================================================================================================================================
# CONFIGURATION
# Translation settings from GitHub Actions environment variables.
#
# (cs)
# Nastavení překladu z proměnných prostředí GitHub Actions.
# ====================================================================================================================================

API = os.environ["TRANSLATE_API"]

SOURCE_FILE = Path(
    os.environ.get(
        "TRANSLATE_SOURCE",
        "README.cs.md"
    )
)

OUTPUT_FILE = Path(
    os.environ.get(
        "TRANSLATE_OUTPUT",
        "README.md"
    )
)

SOURCE_LANG = os.environ.get(
    "TRANSLATE_SOURCE_LANG",
    "cs"
)

TARGET_LANG = os.environ.get(
    "TRANSLATE_TARGET_LANG",
    "en"
)



# ====================================================================================================================================
# CHECK SOURCE FILE
#
# (cs)
# Kontrola zdrojového souboru.
# ====================================================================================================================================

if not SOURCE_FILE.exists():
    print(f"No file to translate: {SOURCE_FILE}")
    exit(0)



print(f"Translating: {SOURCE_FILE}")


text = SOURCE_FILE.read_text(
    encoding="utf-8"
)



# ====================================================================================================================================
# TRANSLATE USING LIBRETRANSLATE API
#
# (cs)
# Překlad pomocí LibreTranslate API.
# ====================================================================================================================================

response = requests.post(
    API,
    data={
        "q": text,
        "source": SOURCE_LANG,
        "target": TARGET_LANG,
        "format": "text"
    },
    timeout=120
)

# response.raise_for_status()


# result = response.json()["translatedText"]


if not response.ok:
    print("LibreTranslate error:")
    print(response.text)
    exit(1)

result = response.json()["translatedText"]




# ====================================================================================================================================
# SAVE RESULT
#
# (cs)
# Uložení přeloženého souboru.
# ====================================================================================================================================

OUTPUT_FILE.write_text(
    result,
    encoding="utf-8"
)


print(f"Done: {OUTPUT_FILE}")