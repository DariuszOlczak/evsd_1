from flask import Flask, render_template, request, jsonify
import pandas as pd
import os
from pathlib import Path
from analysis import Analyzer

app = Flask(__name__)

#Loading clean data using correct path
PROJECT_ROOT = Path(__file__).parent
DATA_PATH = PROJECT_ROOT / 'data' / 'cleaned_data.csv'
try:
    df_clean = pd.read_csv(DATA_PATH)
    analyzer = Analyzer(df_clean)
    print(f"Data loaded successfully. Shape: {df_clean.shape}")
    print(f"Analyzer ready with: {len(analyzer.get_series_name())} series")
except Exception as e:
    print(f"Error loading data. {e}")
    df_clean = None
    analyzer = None



if __name__ == "__main__":
    print()

