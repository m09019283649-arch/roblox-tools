class RobloxError(Exception):
    pass

class InvalidInputError(RobloxError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ResourceNotFoundError(RobloxError):
    def __init__(self, resource_name):
        self.resource_name = resource_name
        self.message = f'Resource {resource_name} not found'
        super().__init__(self.message)

class PermissionDeniedError(RobloxError):
    def __init__(self, action):
        self.action = action
        self.message = f'Permission denied for action: {action}'
        super().__init__(self.message)

def handle_error(error):
    if isinstance(error, InvalidInputError):
        print(f'Invalid input: {error.message}')
    elif isinstance(error, ResourceNotFoundError):
        print(f'Error: {error.message}')
    elif isinstance(error, PermissionDeniedError):
        print(f'Access issue: {error.message}')
    else:
        print('An unknown error occurred.')

