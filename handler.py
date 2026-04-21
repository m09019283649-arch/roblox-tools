import json
import requests

def fetch_roblox_data(asset_id):
    url = f'https://api.roblox.com/marketplace/productinfo?id={{asset_id}}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f'Error fetching data: {e}')
        return None


def parse_roblox_data(data):
    if not data:
        return 'No data available'
    parsed = {
        'name': data.get('Name', 'Unknown'),
        'description': data.get('Description', 'No description'),
        'price': data.get('PriceInRobux', 0),
        'creator': data.get('Creator', {}).get('Name', 'Unknown')
    }
    return json.dumps(parsed, indent=2)


def main(asset_id):
    data = fetch_roblox_data(asset_id)
    result = parse_roblox_data(data)
    print(result)


if __name__ == '__main__':
    asset_id = 12345678  # Sample asset ID
    main(asset_id)
