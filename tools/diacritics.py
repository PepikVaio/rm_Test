from openai import OpenAI
from pathlib import Path
import os

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"]
)

input_file = Path("README.md")
output_file = Path("README_result.md")

text = input_file.read_text(encoding="utf-8")

print("Posílám text do ChatGPT...")

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    temperature=0,
    messages=[
        {
            "role": "system",
            "content": """
Jsi český korektor.

Doplň pouze chybějící českou diakritiku.

Pravidla:
- neměň význam textu
- nepřepisuj věty
- neměň Markdown formátování
- zachovej nadpisy, odrážky a mezery
- vrať pouze opravený text
"""
        },
        {
            "role": "user",
            "content": text
        }
    ]
)

result = response.choices[0].message.content

output_file.write_text(
    result,
    encoding="utf-8"
)

print("Hotovo")