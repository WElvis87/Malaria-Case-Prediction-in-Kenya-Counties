from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.data_loader import load_data

try:
    import src.data_loader as dl
    print("USING MODULE:", dl.__file__)

    df = load_data()
    print("Columns:", df.columns.tolist())

except Exception as e:
    print("Failed to load data", e)