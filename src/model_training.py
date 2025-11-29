import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
from config import load_config

class ModelTrainingError(Exception):
    pass

def create_model():
    config = load_config()
    model_type = config["model"]["type"]
    params = config["model"]["parameters"]

    if model_type == "random-forest":
        model = RandomForestRegressor(**params)
    else:
        raise ModelTrainingError(f"Unsupported model type: {model_type}")

    return model

def train_model(model, X_train, y_train):
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    mse = mean_squared_error(y_test, preds)
    rmse = np.sqrt(mse)

    return {
        "mae": mae,
        "rmse": rmse
    }

def save_model(model):
    config = load_config()
    path = config["output"]["model_dir"]
    joblib.dump(model, path)
    return path
