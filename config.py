import json
import os

def load_config(config_file, default_file):
    if not os.path.exists(config_file):
        with open(default_file, 'r') as df:
            return json.load(df)
    with open(config_file, 'r') as cf:
        return json.load(cf)

# Usage Example:
if __name__ == '__main__':
    config = load_config('config.json', 'default_config.json')
    print(config)