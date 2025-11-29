from data_loader import load_data

try:
    df = load_data()
    print("Data loaded successfully!")
    print("Columns:", df.columns.tolist())
    print("Number of rows:", len(df))
except Exception as e:
    print("Data loading failed:", e)
    