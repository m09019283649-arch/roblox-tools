import json
import requests

class RobloxDataHandler:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_data(self, endpoint):
        response = requests.get(f'{self.base_url}/{endpoint}')
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Error: {response.status_code} - {response.text}')

    def save_data_to_file(self, data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_data_from_file(self, filename):
        with open(filename, 'r') as f:
            return json.load(f)

    def update_data_value(self, filename, key, new_value):
        data = self.load_data_from_file(filename)
        if key in data:
            data[key] = new_value
            self.save_data_to_file(data, filename)
        else:
            raise KeyError(f'Key {key} not found in data')

# Usage Example:
# handler = RobloxDataHandler('https://data.roblox.com')
# data = handler.get_data('example_endpoint')
# handler.save_data_to_file(data, 'data.json')
# handler.update_data_value('data.json', 'example_key', 'new_value')
