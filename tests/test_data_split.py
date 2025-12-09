from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.clean_data import clean_data
from src.load_data import load_data
from src.data_split import split_data

try:
    df = load_data()
    df = clean_data(df)
    X_train, X_test, y_train, y_test = split_data(df)

    print("Data Split Successfully")
    print("X train", len(X_train))
    print("X_test", len(X_test))
    print("Y_Train", len(y_train))
    print("Y_Test", len(y_test))
except Exception as e:
    print("Failed to split the data", e)