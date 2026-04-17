import json
import requests

class RobloxDataProcessor:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_data(self, endpoint):
        response = requests.get(f'{self.base_url}/{endpoint}')
        if response.status_code != 200:
            raise Exception(f'Error fetching data: {response.status_code}')
        return response.json()

    def filter_data(self, data, criteria):
        return [item for item in data if all(item.get(k) == v for k, v in criteria.items())]  

    def save_as_json(self, data, filename):
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def process_data(self, endpoint, criteria, filename):
        data = self.fetch_data(endpoint)
        filtered_data = self.filter_data(data, criteria)
        self.save_as_json(filtered_data, filename)

# Example usage (commented out):
# processor = RobloxDataProcessor('https://api.roblox.com')
# processor.process_data('users', {'isFriend': True}, 'friends.json')
