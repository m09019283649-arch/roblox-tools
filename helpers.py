import json
import random
import string

def generate_random_string(length=10):
    '''Generate a random string of fixed length'''  
    letters = string.ascii_letters  
    return ''.join(random.choice(letters) for i in range(length))


def load_json_file(filepath):
    '''Load JSON data from a file'''  
    with open(filepath, 'r') as file:
        return json.load(file)


def save_json_file(data, filepath):
    '''Save data to a JSON file'''  
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


def pretty_print_json(data):
    '''Pretty print JSON data'''  
    print(json.dumps(data, indent=4))


def flatten_list(nested_list):
    '''Flatten a nested list'''  
    return [item for sublist in nested_list for item in sublist]


def merge_dicts(dict1, dict2):
    '''Merge two dictionaries into one'''  
    return {**dict1, **dict2}