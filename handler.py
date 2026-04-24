import json
import requests

class RobloxDataHandler:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self, endpoint, params=None):
        try:
            response = requests.get(f'{self.api_url}/{endpoint}', params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Error fetching data: {e}')  
            return None

    def save_data(self, filename, data):
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def load_data(self, filename):
        try:
            with open(filename, 'r') as json_file:
                return json.load(json_file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f'Error loading data: {e}')  
            return None

    def get_player_stats(self, player_id):
        endpoint = 'players'
        params = {'id': player_id}
        return self.fetch_data(endpoint, params)