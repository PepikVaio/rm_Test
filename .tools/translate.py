import os
import re
from pathlib import Path
from transformers import MarianMTModel, MarianTokenizer

# =========================
# INPUTS (GitHub Action)
# =========================
MODEL_NAME = os.environ["TRANSLATE_MODEL"]
SOURCE_FILE = Path(os.environ.get("TRANSLATE_SOURCE", "README.cs.md"))
OUTPUT_FILE = Path(os.environ.get("TRANSLATE_OUTPUT", "README.md"))

if not SOURCE_FILE.exists():
    print(f"No file: {SOURCE_FILE}")
    exit(0)

print(f"Translating: {SOURCE_FILE}")

tokenizer = MarianTokenizer.from_pretrained(MODEL_NAME)
model = MarianMTModel.from_pretrained(MODEL_NAME)

# ===================================================================================================
# PROTECT TECHNICAL TEXT
# Temporarily replaces technical elements with placeholders before translation.
# Prevents the translation model from modifying code, paths, extensions, and project specific names.
#
# (cs)
# Dočasně nahradí technické prvky zástupnými značkami před překladem.
# Zabrání překladači upravovat kód, cesty, přípony a názvy projektů.
# ===================================================================================================
def protect_text(text):

    protected = {}

    patterns = [
        r"`[^`]+`",
        r"/[A-Za-z0-9_./-]+",
        r"\.[a-zA-Z0-9]+",
        r"\bXovi\b",
        r"\bQt\b",
        r"\bQML\b",
    ]

    counter = 0

    for pattern in patterns:
        for match in re.findall(pattern, text):

            key = f"PLACEHOLDER_{counter}"

            protected[key] = match

            text = text.replace(
                match,
                key
            )

            counter += 1

    return text, protected

def restore_text(text, protected):

    for key, value in protected.items():
        text = text.replace(
            key,
            value
        )

    return text

# ===========================================================================
# TRANSLATE TEXT
# Translates a single text block while keeping protected elements unchanged.
#
# (cs)
# Přeloží jeden blok textu a zachová chráněné prvky beze změny.
# ===========================================================================
def translate_text(text):

    if not text.strip():
        return text
    
    original, protected = protect_text(text)

    inputs = tokenizer(
        original,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    translated = model.generate(
        **inputs,
        max_length=512,
        num_beams=4
    )

    result = tokenizer.decode(
        translated[0],
        skip_special_tokens=True
    )

    return restore_text(result, protected)

# ==============================================================================================
# TRANSLATE MARKDOWN DOCUMENT
# Processes Markdown line by line while preserving Markdown formatting.
# Code blocks are skipped, headings keep their original markers, and empty lines are preserved.
#
# (cs)
# Zpracuje Markdown dokument řádek po řádku při zachování formátování Markdownu.
# Bloky kódu se přeskočí, nadpisy zachovají své značky a prázdné řádky zůstanou.
# ==============================================================================================
def translate_markdown(text):

    result = []

    in_code = False

    for line in text.splitlines():

        if line.startswith("```"):
            in_code = not in_code
            result.append(line)
            continue

        if in_code:
            result.append(line)
            continue

        if line.startswith("#"):
            prefix = re.match(r"^#+\s*", line).group()
            content = line[len(prefix):]

            result.append(
                prefix + translate_text(content)
            )
            continue

        if not line.strip():
            result.append(line)
            continue

        result.append(
            translate_text(line)
        )

    return "\n".join(result)

# =============================================================================================================
# READ SOURCE FILE AND WRITE TRANSLATED OUTPUT
# Reads the source Markdown file, translates its content, and saves the translated version to the output file.
#
# (cs)
# Načte zdrojový Markdown soubor, přeloží jeho obsah a uloží přeloženou verzi do výstupního souboru.
# =============================================================================================================
text = SOURCE_FILE.read_text(
    encoding="utf-8"
)

translated = translate_markdown(text)

OUTPUT_FILE.write_text(
    translated,
    encoding="utf-8"
)

print(f"Done: {OUTPUT_FILE}")