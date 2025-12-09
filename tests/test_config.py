from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.config import load_config

try:
    config = load_config()

    print(config["project"]["name"])
    print(config["data"]["raw"])
    
except Exception as e:
    print("Failed to load config file", e)