from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.data_cleaning import clean_data
from src.data_loader import load_data
from src.data_split import split_data
from src.model_training import train_model, create_model, evaluate_model

try:
    df = load_data()
    df = clean_data(df)
    X_train, X_test, y_train, y_test = split_data(df)
    model = create_model()
    model = train_model(model, X_train, y_train)
    mae, mse, r2, rmse = evaluate_model(model, X_test, y_test)

    print("Model Created Successfully")
    print("Mean Absolute Error:", mae)
    print("Mean Squared Error:", mse)
    print("RMSE:", rmse)
    print("R2:", r2)
     
except Exception as e:
    print("Failed to train model", e)