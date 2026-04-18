def validate_input(input_data):
    if not isinstance(input_data, dict):
        raise ValueError('Input must be a dictionary')
    if 'username' not in input_data or not isinstance(input_data['username'], str):
        raise ValueError('Missing or invalid username')
    if 'age' not in input_data or not isinstance(input_data['age'], int) or input_data['age'] < 0:
        raise ValueError('Missing or invalid age')
    if 'score' not in input_data or not isinstance(input_data['score'], (int, float)):
        raise ValueError('Missing or invalid score')

# Example of main processing loop
input_list = [
    {'username': 'Player1', 'age': 21, 'score': 1500},
    {'username': 'Player2', 'age': -5, 'score': 2000},
    'InvalidInput',
    {'username': 'Player3', 'score': 3000},
]

for input_data in input_list:
    try:
        validate_input(input_data)
        print(f'Validated input: {input_data}')
    except ValueError as e:
        print(f'Input validation error: {e}')