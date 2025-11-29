import pandas as pd
from config import load_config
from pathlib import Path

class DataLoaderError(Exception):
    pass

def load_data(path: str = None) -> pd.DataFrame:
    config = load_config()

    if path is None:
        path = Path(config["data"]["raw"])
    else:
        path = Path(path)
    
    if not path.exists():
        raise DataLoaderError(f"Data not found at {path}")
    
    df = pd.read_csv(path)

    required_columns = config["features"] + [config["target"]]
    missing = [col for col in required_columns if col not in df.columns]

    if missing:
        raise DataLoaderError(f"Missing required columns: {missing}")

    return df