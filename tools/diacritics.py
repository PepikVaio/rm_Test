from pathlib import Path
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch


INPUT = Path("README.md")
OUTPUT = Path("README_result.md")


MODEL = "google/mt5-small"


print("Načítám model...")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL,
    use_fast=False,
    legacy=True
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL
)


text = INPUT.read_text(
    encoding="utf-8"
)


print("Zpracovávám text...")


prompt = f"""
Doplň českou diakritiku v tomto textu.

Pravidla:
- zachovej význam
- neměň věty
- zachovej Markdown formátování
- vrať pouze opravený text

Text:

{text}
"""


inputs = tokenizer(
    prompt,
    return_tensors="pt",
    truncation=True,
    max_length=512
)


with torch.no_grad():

    output = model.generate(
        **inputs,
        max_length=512,
        num_beams=4
    )


result = tokenizer.decode(
    output[0],
    skip_special_tokens=True
)


OUTPUT.write_text(
    result,
    encoding="utf-8"
)


print("Hotovo")