from pathlib import Path
from transformers import pipeline

input_file = Path("README.md")
output_file = Path("README_result.md")

text = input_file.read_text(encoding="utf-8")

print("Načten text:")
print(text[:200])

print("Načítám model...")

model = pipeline(
    "text2text-generation",
    model="Helsinki-NLP/opus-mt-en-cs"
)

result = model(text, max_length=512)

output = result[0]["generated_text"]

output_file.write_text(output, encoding="utf-8")

print("Hotovo")
