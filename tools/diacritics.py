from pathlib import Path
import subprocess
import shutil


INPUT = Path("README.md")
OUTPUT = Path("README_result.md")

UFAL = Path("tools/ufal")


print("Kontrola UFAL nástroje...")


if not UFAL.exists():
    raise Exception("UFAL nástroj nebyl nalezen")


print("Spouštím obnovu diakritiky...")


subprocess.run(
    [
        "python",
        str(UFAL / "restore.py"),
        str(INPUT),
        str(OUTPUT)
    ],
    check=True
)


print("Hotovo")