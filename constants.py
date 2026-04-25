BASE_URL = 'https://api.roblox.com/'

PAGE_SIZE = 100

MAX_RETRIES = 5

RETRY_DELAY = 2  # seconds

ERROR_CODES = {
    400: 'Bad Request',
    401: 'Unauthorized',
    403: 'Forbidden',
    404: 'Not Found',
    500: 'Internal Server Error',
    503: 'Service Unavailable',
}

DEFAULT_TIMEOUT = 10  # seconds

SUPPORTED_PLATFORMS = ['PC', 'Mobile', 'Xbox', 'VR']

GAME_GENRES = [
    'Action',
    'Adventure',
    'Role Playing',
    'Simulation',
    'Horror',
    'Strategy',
    'Tycoon',
    'Obby',
]