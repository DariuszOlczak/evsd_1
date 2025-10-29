import os
from pathlib import Path

PROJECT_ROOT = Path().absolute()
DATA_DIR = PROJECT_ROOT / 'data'
OUTPUT_DIR = PROJECT_ROOT / 'output'
DATA_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

CLEANED_DATA_PATH = DATA_DIR / 'cleaned_data.csv'
ORIGINAL_DATA_PATH = DATA_DIR / 'original_data.csv'

print(f"Project root: {PROJECT_ROOT}")
print(f"Data dir: {DATA_DIR}")
print(f"Cleaned Data dir: {CLEANED_DATA_PATH}")
