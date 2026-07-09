from pathlib import Path
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL = "SEM_DAME_CESKY_MODEL"

input_file = Path("README.md")
output_file = Path("README_result.md")

text = input_file.read_text(encoding="utf-8")

tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL)

tokens = tokenizer(
    text,
    return_tensors="pt",
    truncation=True
)

result = model.generate(
    **tokens,
    max_length=1024
)

output = tokenizer.decode(
    result[0],
    skip_special_tokens=True
)

output_file.write_text(output, encoding="utf-8")
