from pathlib import Path
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

input_file = Path("README.md")
output_file = Path("README_result.md")

text = input_file.read_text(encoding="utf-8")

print("Načten text:")
print(text)

print("Načítám model...")

model_name = "Helsinki-NLP/opus-mt-en-cs"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

inputs = tokenizer(
    text,
    return_tensors="pt",
    truncation=True
)

translated = model.generate(
    **inputs,
    max_length=512
)

output = tokenizer.decode(
    translated[0],
    skip_special_tokens=True
)

output_file.write_text(output, encoding="utf-8")

print("Hotovo")
