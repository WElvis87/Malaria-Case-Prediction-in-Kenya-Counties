from data_loader import load_data
from data_cleaning import clean_data
from data_split import split_data
from model_training import create_model, train_model, evaluate_model, save_model

def run_pipeline():
    print("=== Starting Climalaria Pipeline ===")

    df = load_data()
    print("Data loaded:", df.shape)

    df = clean_data(df)
    print("Data cleaned:", df.shape)

    X_train, X_test, y_train, y_test = split_data(df)
    print(f"Data split: Train={len(X_train)}, Test={len(X_test)}")

    model = create_model()
    print("Model created.")

    model = train_model(model, X_train, y_train)
    print("Model trained.")

    metrics = evaluate_model(model, X_test, y_test)
    print(f"Evaluation metrics: MAE={metrics['mae']:.2f}, RMSE={metrics['rmse']:.2f}")

    path = save_model(model)
    print(f"Model saved to {path}")

    print("=== Pipeline completed ===")

    return model, metrics

if __name__ == "__main__":
    run_pipeline()
