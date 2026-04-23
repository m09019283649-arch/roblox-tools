import json
import os

DEFAULT_CONFIG = {
    'username': 'guest',
    'max_players': 10,
    'game_mode': 'classic',
    'sound_enabled': True,
    'graphics_quality': 'high'
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = DEFAULT_CONFIG.copy()
        self.load_configuration()

    def load_configuration(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                user_config = json.load(file)
                self.config.update(user_config)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value

    def save(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)

# Example of usage:
# config_loader = ConfigLoader()
# print(config_loader.get('username'))
# config_loader.set('username', 'Player1')
# config_loader.save()