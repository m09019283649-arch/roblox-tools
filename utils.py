import json

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged


def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]


def generate_unique_id(prefix='id', existing_ids=None):
    import uuid
    existing_ids = existing_ids or set()
    unique_id = f'{prefix}_{uuid.uuid4()}'
    while unique_id in existing_ids:
        unique_id = f'{prefix}_{uuid.uuid4()}'
    return unique_id

