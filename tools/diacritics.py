from pathlib import Path

input_file = Path("README.md")
output_file = Path("README_result.md")

text = input_file.read_text(encoding="utf-8")

# zatím jen test průchodu
output_file.write_text(text, encoding="utf-8")

print("Hotovo")
