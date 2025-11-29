import pandas as pd
from config import load_config

class DataCleaningError(Exception):
    pass

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    config = load_config()

    df = df.copy()

    required_columns = config["features"] + [config["target"]]

    missing_columns = [c for c in required_columns if c not in df.columns]

    if missing_columns:
        raise DataCleaningError(f"Missing Columns {missing_columns} from dataframe")
    
    df = df.dropna(subset=required_columns)

    df = df.drop_duplicates()

    df.reset_index(drop=True, inplace=True)
    return df
