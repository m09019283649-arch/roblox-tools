BASE_URL = 'https://api.roblox.com/'

ROLES = {
    'admin': 1,
    'moderator': 2,
    'user': 3,
}

GAME_INFO_KEYS = [
    'name',
    'id',
    'creator',
    'playerCount',
    'maxPlayers',
    'description',
]

ITEM_TYPES = {
    'clothing': 1,
    'accessory': 2,
    'gear': 3,
    'model': 4,
}

def get_role_name(role_id):
    for role, id in ROLES.items():
        if id == role_id:
            return role
    return 'unknown'

def get_game_info_key(index):
    try:
        return GAME_INFO_KEYS[index]
    except IndexError:
        return 'invalid_key'

def is_item_type(item_type):
    return item_type in ITEM_TYPES.keys()

