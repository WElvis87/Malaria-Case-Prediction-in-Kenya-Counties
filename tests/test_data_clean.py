from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.clean_data import clean_data
from src.load_data import load_data

try:
    df = load_data()
    df = clean_data(df)
    print("Data Cleaned Successfully")
except Exception as e:
    print(f"Failed to Clean the data", e)