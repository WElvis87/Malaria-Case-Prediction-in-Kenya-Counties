import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.config import load_config

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
    r2 = r2_score(y_test, preds)
    rmse = np.sqrt(mse)

    return mae, mse, r2, rmse

def create_evaluation_report(mae, mse, rmse, r2, mape=None, residual_summary=None, output_path=None):
    config = load_config()

    if output_path is None:
        output_path = config["output"]["evaluation_report"]

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Model Performance Evaluation Report (Regression)\n\n")

        f.write("## Error Metrics\n")
        f.write(f"- Mean Absolute Error (MAE): {mae:.3f}\n")
        f.write(f"- Mean Squared Error (MSE): {mse:.3f}\n")
        f.write(f"- Root Mean Squared Error (RMSE): {rmse:.3f}\n")
        f.write(f"- R² Score: {r2:.3f}\n")

        if mape is not None:
            f.write(f"- Mean Absolute Percentage Error (MAPE): {mape:.2f}%\n")

        f.write("\n")

        if residual_summary is not None:
            f.write("## Residual Analysis\n")
            f.write(f"{residual_summary}\n\n")

        f.write("## Interpretation\n")
        f.write(
            f"The model explains approximately {r2:.1%} of the variance in the target variable. "
            f"On average, predictions deviate from the true values by about {mae:.3f} units. "
            f"The RMSE of {rmse:.3f} indicates sensitivity to larger errors, which should be "
            f"evaluated against domain-specific tolerance thresholds.\n"
        )

    print(f"Report generated: {output_path}")


def save_model(model):
    config = load_config()
    path = config["output"]["model_dir"]
    joblib.dump(model, path)
    return path
