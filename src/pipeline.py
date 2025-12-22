from data_loader import load_data
from data_cleaning import clean_data
from data_split import split_data
from model_training import create_model, train_model, evaluate_model, save_model, create_evaluation_report

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

    mae, mse, rmse, r2 = evaluate_model(model, X_test, y_test)

    create_evaluation_report(mae, mse, rmse, r2)

    path = save_model(model)
    print(f"Model saved to {path}")

    print("=== Pipeline completed ===")

    return model

if __name__ == "__main__":
    run_pipeline()
