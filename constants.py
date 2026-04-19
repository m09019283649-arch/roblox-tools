GAME_ID = 123456789

MAX_PLAYERS = 30

SERVER_NAME = 'MyRobloxServer'

SPECIAL_ITEMS = {
    'GoldSword': {
        'value': 100,
        'type': 'weapon',
        'description': 'A shiny golden sword!'
    },
    'MagicPotion': {
        'value': 50,
        'type': 'consumable',
        'description': 'A potion that restores health!'
    }
}

DEFAULT_CONFIG = {
    'gameMode': 'adventure',
    'difficulty': 'normal',
    'maxTime': 120,
    'enableChat': True
}

ITEM_COLORS = {
    'GoldSword': '#FFD700',
    'MagicPotion': '#8A2BE2'
}

PLAYER_ROLES = [
    'admin',
    'moderator',
    'player'
]

REGION_NAMES = [
    'Town',
    'Forest',
    'Dungeon'
]

DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/your_webhook_here'

WINNING_CONDITIONS = [
    'collect_all_items',
    'defeat_boss',
    'complete_time_challenge'
]