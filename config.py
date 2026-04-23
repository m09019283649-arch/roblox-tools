import json
import os

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = self.load_config()

    def load_config(self):
        config_path = 'config.json'
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                user_config = json.load(f)
            return self.merge_configs(self.default_config, user_config)
        return self.default_config

    def merge_configs(self, default, user):
        merged = default.copy()
        for key, value in user.items():
            if isinstance(value, dict) and key in merged:
                merged[key] = self.merge_configs(merged[key], value)
            else:
                merged[key] = value
        return merged

# Example default configuration
default_config = {
    'setting1': True,
    'setting2': 42,
    'nested': {
        'sub_setting1': 'default',
        'sub_setting2': 3.14
    }
}

# Load configuration
config_loader = ConfigLoader(default_config)
config = config_loader.config
