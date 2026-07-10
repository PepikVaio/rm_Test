from pathlib import Path
import os

import torch
from transformers import MarianMTModel, MarianTokenizer


# ====================================================================================================================================
# CONFIGURATION
# Translation settings from GitHub Actions environment variables.
#
# (cs)
# Nastavení překladu z proměnných prostředí GitHub Actions.
# ====================================================================================================================================

MODEL_NAME = os.environ["TRANSLATE_MODEL"]

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


# ====================================================================================================================================
# LOAD MODEL
#
# (cs)
# Načtení překladového modelu.
# ====================================================================================================================================

print("Loading translation model...")

tokenizer = MarianTokenizer.from_pretrained(
    MODEL_NAME
)

model = MarianMTModel.from_pretrained(
    MODEL_NAME
)


# ====================================================================================================================================
# TRANSLATE
#
# (cs)
# Překlad textu.
# ====================================================================================================================================

text = SOURCE_FILE.read_text(
    encoding="utf-8"
)


inputs = tokenizer(
    text,
    return_tensors="pt",
    truncation=True,
    max_length=512
)


with torch.no_grad():

    translated = model.generate(
        **inputs,
        max_length=512,
        num_beams=4
    )


result = tokenizer.decode(
    translated[0],
    skip_special_tokens=True
)


# ====================================================================================================================================
# SAVE RESULT
#
# (cs)
# Uložení výsledku.
# ====================================================================================================================================

OUTPUT_FILE.write_text(
    result,
    encoding="utf-8"
)


print(f"Done: {OUTPUT_FILE}")