class RobloxError(Exception):
    """
    Base class for all exceptions related to Roblox.
    """
    pass

class UserNotFoundError(RobloxError):
    """
    Exception raised when a user cannot be found.
    """
    def __init__(self, username):
        super().__init__(f'User not found: {username}')
        self.username = username

class PermissionDeniedError(RobloxError):
    """
    Exception raised when a user lacks permission.
    """
    def __init__(self, action):
        super().__init__(f'Permission denied for action: {action}')
        self.action = action

class InvalidGameIdError(RobloxError):
    """
    Exception raised for invalid game IDs.
    """
    def __init__(self, game_id):
        super().__init__(f'Invalid game ID: {game_id}')
        self.game_id = game_id

class InvalidAssetError(RobloxError):
    """
    Exception raised for invalid asset references.
    """
    def __init__(self, asset_name):
        super().__init__(f'Invalid asset: {asset_name}')
        self.asset_name = asset_name

class RequestTimeoutError(RobloxError):
    """
    Exception raised for request timeouts.
    """
    def __init__(self, url):
        super().__init__(f'Request to {url} timed out')
        self.url = url