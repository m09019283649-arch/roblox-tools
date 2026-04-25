import json
import os

DEFAULT_CONFIG = {
    'server_host': 'localhost',
    'server_port': 8080,
    'debug_mode': False,
    'max_users': 50,
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                user_config = json.load(f)
            return {**DEFAULT_CONFIG, **user_config}
        return DEFAULT_CONFIG

    def get(self, key, default=None):
        return self.config.get(key, default)

config_loader = ConfigLoader()

if __name__ == '__main__':
    print(config_loader.config)