from pathlib import Path
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL = "imvladikon/word-level-czech-diacritics"

input_file = Path("README.md")
output_file = Path("README_result.md")

text = input_file.read_text(encoding="utf-8")

print("Načítám model...")

tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL)

print("Zpracovávám text...")

tokens = tokenizer(
    text,
    return_tensors="pt",
    truncation=True,
    max_length=512
)

result = model.generate(
    **tokens,
    max_length=512
)

output = tokenizer.decode(
    result[0],
    skip_special_tokens=True
)

output_file.write_text(output, encoding="utf-8")

print("Hotovo")