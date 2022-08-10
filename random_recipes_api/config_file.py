CONFIG_PATH:str = 'config.json'
from typing import Dict, Any
import json


def get_data() -> Dict[str, Any]:
    with open(CONFIG_PATH, "r") as jsonfile:
        data = json.load(jsonfile)
        return data