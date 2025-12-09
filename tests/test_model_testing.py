from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.clean_data import clean_data
from src.load_data import load_data
from src.data_split import split_data
from src.train_model import train_model, create_model, evaluate_model

try:
    df = load_data()
    df = clean_data(df)
    X_train, X_test, y_train, y_test = split_data(df)
    model = create_model()
    model = train_model(model, X_train, y_train)
    metrics = evaluate_model(model, X_test, y_test)
    mae = metrics["mae"]
    rmse = metrics["rmse"]

    print("Model Created Successfully")
    print("Mean Absolute Error:", mae)
    print("RMSE:", rmse)
     
except Exception as e:
    print("Failed to train model", e)