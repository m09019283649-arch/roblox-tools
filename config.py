import os

class Config:
    def __init__(self):
        self.environment = self.get_env()
        self.db_uri = self.get_db_uri()
        self.api_key = self.get_api_key()

    def get_env(self):
        return os.getenv('ENVIRONMENT', 'development')

    def get_db_uri(self):
        return os.getenv('DATABASE_URI', 'sqlite:///db.sqlite')

    def get_api_key(self):
        if self.environment == 'production':
            return os.getenv('API_KEY')
        return 'test-api-key'

config = Config()