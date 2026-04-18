class RobloxError(Exception):
    """Base class for all Roblox-related exceptions."""
    pass

class DataNotFoundError(RobloxError):
    """Raised when the requested data is not found."""
    def __init__(self, data_key):
        self.data_key = data_key
        super().__init__(f'Data not found for key: {data_key}')

class InvalidDataFormatError(RobloxError):
    """Raised when data format is invalid."""
    def __init__(self, expected_format, received_format):
        self.expected_format = expected_format
        self.received_format = received_format
        super().__init__(f'Expected format: {expected_format}, but received: {received_format}')

class APIRequestError(RobloxError):
    """Raised when an API request fails."""
    def __init__(self, status_code, message='API request failed'): 
        self.status_code = status_code
        super().__init__(f'{message} - Status code: {status_code}')