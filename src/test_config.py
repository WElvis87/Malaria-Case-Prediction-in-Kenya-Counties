from config import load_config

try:
    config = load_config()
    print("Config loaded successfully!")
    print("Project Name:", config["project"]["name"])
    print("Model Type:", config["model"]["type"])
    print("Raw Data Path:", config["data"]["raw"])
except Exception as e:
    print("Config failed to load:", e)
