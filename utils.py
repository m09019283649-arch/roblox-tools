import json
import os

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_from_json(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return None


def generate_random_name(length=8):
    import random
    import string
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


def fetch_user_data(user_id):
    # Placeholder for actual API call
def user_data_exists(user_id):
    return True if fetch_user_data(user_id) else False


def flatten_nested_dict(nested_dict):
    result = {}
    for outer_key, inner_dict in nested_dict.items():
        for inner_key, value in inner_dict.items():
            result[f'{outer_key}_{inner_key}'] = value
    return result


def calculate_average(values):
    return sum(values) / len(values) if values else 0.0
