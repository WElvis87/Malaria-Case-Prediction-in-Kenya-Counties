from sklearn.model_selection import train_test_split
from config import load_config

class DataSplitError(Exception):
    pass

def split_data(df):
    config = load_config()

    target = config["target"]
    features = config["features"]

    if target not in df.columns:
        raise DataSplitError(f"Target column '{target}' missing from dataframe.")

    missing = [c for c in features if c not in df.columns]
    if missing:
        raise DataSplitError(f"Feature columns missing: {missing}")

    X = df[features]
    y = df[target]

    params = config["split"]

    test_size = params.get("test_size", 0.2)
    shuffle = params.get("shuffle", False)
    random_state = params.get("random_state", 42)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=test_size,
        shuffle=shuffle,
        random_state=random_state
    )

    return X_train, X_test, y_train, y_test
