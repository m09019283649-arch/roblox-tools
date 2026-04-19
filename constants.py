from typing import Dict, Any

# Constants used throughout the Roblox tools

BASE_URL: str = 'https://www.roblox.com'

# Status codes used for HTTP requests
STATUS_CODES: Dict[str, int] = {
    'OK': 200,
    'CREATED': 201,
    'ACCEPTED': 202,
    'NO_CONTENT': 204,
    'BAD_REQUEST': 400,
    'UNAUTHORIZED': 401,
    'FORBIDDEN': 403,
    'NOT_FOUND': 404,
}

# Default timeout settings for HTTP requests
DEFAULT_TIMEOUT: float = 5.0

def get_status_message(code: int) -> str:
    """
    Retrieve HTTP status message based on code.

    Args:
        code (int): The HTTP status code.

    Returns:
        str: A message corresponding to the HTTP status code.
    """
    messages: Dict[int, str] = {
        200: 'OK',
        201: 'Created',
        202: 'Accepted',
        204: 'No Content',
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found',
    }
    return messages.get(code, 'Unknown Status')

API_VERSION: str = 'v1'

# Commonly used game IDs
GAME_IDS: Dict[str, int] = {
    'ROBLOX': 1,
    'MEETUP': 2,
    'NINJA': 3,
}
