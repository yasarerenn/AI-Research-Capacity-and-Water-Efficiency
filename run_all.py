from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
scripts = [
    "01_descriptives.py",
    "02_main_models.py",
    "03_sectoral_models.py",
    "04_robustness.py",
    "05_figures.py",
]

for script in scripts:
    print(f"\n--- {script} ---")
    subprocess.run([sys.executable, str(root / "code" / script)], check=True)
