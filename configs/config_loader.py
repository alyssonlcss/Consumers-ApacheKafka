import json
PATH = "../configs/appsettings.json"
 
class ConfigLoader:
    @staticmethod
    def load_config(PATH):
        with open(PATH, 'r') as file:
            config = json.load(file)
        return config
