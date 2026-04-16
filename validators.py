import json
import re

class RobloxDataValidator:
    def __init__(self):
        self.username_pattern = r'^[A-Za-z0-9_.]{3,20}$'
        self.asset_id_pattern = r'^\d+$'
        self.max_char_length = 100

    def validate_username(self, username):
        if re.match(self.username_pattern, username):
            return True
        raise ValueError('Invalid Username: Username must be 3-20 characters long and can only contain letters, numbers, underscores, and periods.')

    def validate_asset_id(self, asset_id):
        if re.match(self.asset_id_pattern, asset_id):
            return True
        raise ValueError('Invalid Asset ID: Asset ID must be a numeric string.')

    def validate_description(self, description):
        if isinstance(description, str) and len(description) <= self.max_char_length:
            return True
        raise ValueError('Invalid Description: Description must be a string and cannot exceed 100 characters.')

def validate_roblox_data(data):
    validator = RobloxDataValidator()
    try:
        validator.validate_username(data['username'])
        validator.validate_asset_id(data['asset_id'])
        validator.validate_description(data['description'])
        return json.dumps({'status': 'success', 'message': 'Data is valid.'})
    except ValueError as e:
        return json.dumps({'status': 'error', 'message': str(e)})