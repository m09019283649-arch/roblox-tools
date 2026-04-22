import time
import random
import requests

def retry_request(url, method='GET', data=None, max_retries=5, backoff_factor=0.3):
    retries = 0
    while retries < max_retries:
        try:
            if method.upper() == 'POST':
                response = requests.post(url, json=data)
            else:
                response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Retry {retries + 1}/{max_retries} for {url} - Error: {e}')
            retries += 1
            time.sleep(backoff_factor * (2 ** (retries - 1)) + random.uniform(0, 1))
    raise Exception(f'Max retries exceeded for {url}')
