import json
PATH = "appsettings.json"
 
class ConfigLoader:
    @staticmethod
    def load_config():
        with open(PATH, 'r') as file:
            config = json.load(file)
        return config
