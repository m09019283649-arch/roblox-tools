import json
import re

class RobloxValidator:
    @staticmethod
    def validate_username(username: str) -> bool:
        return bool(re.match(r'^[a-zA-Z][a-zA-Z0-9_]{2,19}$', username))

    @staticmethod
    def validate_password(password: str) -> bool:
        return (6 <= len(password) <= 20) and any(c.isdigit() for c in password)

    @staticmethod
    def validate_game_data(game_data: dict) -> bool:
        required_keys = {'name', 'creator', 'description', 'placeCount'}
        return required_keys.issubset(game_data.keys())

    @staticmethod
    def validate_json(data: str) -> bool:
        try:
            json.loads(data)
            return True
        except json.JSONDecodeError:
            return False

# Example usage of the validators
if __name__ == '__main__':
    print(RobloxValidator.validate_username('player123'))  # True
    print(RobloxValidator.validate_password('pass123'))  # True
    print(RobloxValidator.validate_game_data({'name': 'Cool Game', 'creator': 'dev', 'description': 'Fun!', 'placeCount': 10}))  # True
    print(RobloxValidator.validate_json('{"key": "value"}'))  # True