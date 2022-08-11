import uvicorn
from random_recipes_api import config_file
from typing import Dict, Any


CONFIG_DATA:Dict[str, Any] = config_file.get_data()
port:int = CONFIG_DATA['port']
host:str = CONFIG_DATA['host']


if __name__ == "__main__":
    uvicorn.run("server:app", 
                port=port, 
                host=host, 
                log_level="info")