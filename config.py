import os

class Config:
    BASE_URL = os.getenv('BASE_URL', 'https://default.roblox.com')
    API_KEY = os.getenv('API_KEY', 'your-api-key')
    TIMEOUT = int(os.getenv('TIMEOUT', 30))

    @staticmethod
    def validate_config():
        if not Config.API_KEY:
            raise ValueError('API_KEY cannot be empty')
        if Config.TIMEOUT <= 0:
            raise ValueError('TIMEOUT must be a positive integer')

    @classmethod
    def display_config(cls):
        print(f'Base URL: {cls.BASE_URL}')
        print(f'API Key: {cls.API_KEY}')
        print(f'Timeout: {cls.TIMEOUT}')