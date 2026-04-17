import json

class RobloxError(Exception):
    pass

class ItemNotFoundError(RobloxError):
    pass

class InvalidDataError(RobloxError):
    pass

class RobloxHandler:
    def __init__(self, data):
        self.data = data

    def fetch_item(self, item_id):
        try:
            if not isinstance(item_id, int) or item_id <= 0:
                raise InvalidDataError('Item ID must be a positive integer.')
            item = self.data.get(item_id)
            if item is None:
                raise ItemNotFoundError(f'Item with ID {item_id} not found.')
            return item
        except (InvalidDataError, ItemNotFoundError) as e:
            return json.dumps({'error': str(e)})

    def add_item(self, item_id, item):
        try:
            if not isinstance(item_id, int) or item_id <= 0:
                raise InvalidDataError('Item ID must be a positive integer.')
            if item_id in self.data:
                raise ItemNotFoundError(f'Item with ID {item_id} already exists.')
            self.data[item_id] = item
            return json.dumps({'success': 'Item added successfully.'})
        except (InvalidDataError, ItemNotFoundError) as e:
            return json.dumps({'error': str(e)})

# Example usage
if __name__ == '__main__':
    handler = RobloxHandler({})
    print(handler.add_item(-1, {}))  # Invalid ID
    print(handler.fetch_item(1))  # Not found
    print(handler.add_item(1, {'name': 'Sword'}))  # Success
    print(handler.fetch_item(1))  # Fetch success
