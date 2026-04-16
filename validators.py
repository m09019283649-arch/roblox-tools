def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    if len(user_input) < 3:
        raise ValueError('Input must be at least 3 characters long')
    if any(char.isdigit() for char in user_input):
        raise ValueError('Input must not contain numbers')
    return True

def main_loop():
    while True:
        try:
            user_input = input('Enter a command: ')
            validate_input(user_input)
            process_command(user_input)
        except ValueError as e:
            print(f'Error: {e}')
        except KeyboardInterrupt:
            print('\nExiting program.')
            break

if __name__ == '__main__':
    main_loop()

def process_command(cmd):
    print(f'Processing command: {cmd}')