import requests
import time
import random

def retry_request(func):
    def wrapper(*args, **kwargs):
        retries = 5
        delay = 1
        for attempt in range(retries):
            try:
                return func(*args, **kwargs)
            except requests.RequestException as e:
                if attempt < retries - 1:
                    wait_time = delay + random.uniform(0, 1)
                    print(f'Attempt {attempt + 1} failed: {e}. Retrying in {wait_time:.2f} seconds...')
                    time.sleep(wait_time)
                else:
                    print('All retry attempts failed.')
                    raise
    return wrapper

@retry_request
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()  # Will raise an exception for HTTP errors
    return response.json()

if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = fetch_data(url)
        print(data)
    except Exception as e:
        print(f'Failed to fetch data: {e}')