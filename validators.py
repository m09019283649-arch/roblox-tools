import re

class InputValidationError(Exception):
    pass

def validate_username(username):
    if not isinstance(username, str):
        raise InputValidationError('Username must be a string.')
    if not re.match('^[a-zA-Z0-9_]{3,20}$', username):
        raise InputValidationError('Username must be 3-20 characters long and can contain letters, numbers, and underscores.')


def validate_password(password):
    if not isinstance(password, str):
        raise InputValidationError('Password must be a string.')
    if len(password) < 8:
        raise InputValidationError('Password must be at least 8 characters long.')
    if not re.search('[A-Za-z]', password) or not re.search('[0-9]', password):
        raise InputValidationError('Password must contain both letters and numbers.')


def validate_input(username, password):
    validate_username(username)
    validate_password(password)  
    return True  

# Main processing loop example
if __name__ == '__main__':
    try:
        user_input = ('test_user', 'Pass1234')  # Example input
        validate_input(*user_input)
        print('Input is valid.')
    except InputValidationError as e:
        print(f'Input validation error: {e}')
