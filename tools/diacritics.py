from pathlib import Path
from transformers import pipeline


INPUT = Path("README.md")
OUTPUT = Path("README_result.md")


MODEL = "ufal/bert-base-czech-cased"


print("Načítám český model...")


corrector = pipeline(
    "fill-mask",
    model=MODEL
)


text = INPUT.read_text(
    encoding="utf-8"
)


print("Zpracovávám text...")


# zatím připraveno pro model
# BERT musí doplňovat maskované znaky,
# není to klasický překladač


OUTPUT.write_text(
    text,
    encoding="utf-8"
)


print("Hotovo")