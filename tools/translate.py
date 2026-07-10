from pathlib import Path
import os
import re

from transformers import MarianMTModel, MarianTokenizer


MODEL_NAME = os.environ["TRANSLATE_MODEL"]

SOURCE_FILE = Path(
    os.environ.get("TRANSLATE_SOURCE", "README.cs.md")
)

OUTPUT_FILE = Path(
    os.environ.get("TRANSLATE_OUTPUT", "README.md")
)


if not SOURCE_FILE.exists():
    print(f"No file: {SOURCE_FILE}")
    exit(0)


print(f"Translating: {SOURCE_FILE}")


tokenizer = MarianTokenizer.from_pretrained(
    MODEL_NAME
)

model = MarianMTModel.from_pretrained(
    MODEL_NAME
)


def translate_text(text):

    if not text.strip():
        return text

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    translated = model.generate(
        **inputs,
        max_length=512,
        num_beams=4
    )

    return tokenizer.decode(
        translated[0],
        skip_special_tokens=True
    )


def translate_markdown(text):

    result = []

    in_code = False

    for line in text.splitlines():

        # Markdown code block
        if line.startswith("```"):
            in_code = not in_code
            result.append(line)
            continue


        # Kód nepřekládat
        if in_code:
            result.append(line)
            continue


        # Nadpisy ponechat znak #, překládat text
        if line.startswith("#"):
            prefix = re.match(r"^#+\s*", line).group()
            content = line[len(prefix):]

            result.append(
                prefix + translate_text(content)
            )
            continue


        # Prázdné řádky
        if not line.strip():
            result.append(line)
            continue


        # Normální text
        result.append(
            translate_text(line)
        )


    return "\n".join(result)


text = SOURCE_FILE.read_text(
    encoding="utf-8"
)


translated = translate_markdown(text)


OUTPUT_FILE.write_text(
    translated,
    encoding="utf-8"
)


print(f"Done: {OUTPUT_FILE}")