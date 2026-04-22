import time
import requests

class NetworkException(Exception):
    pass

def request_with_retry(url, retries=3, delay=2):
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            attempt += 1
            if attempt == retries:
                raise NetworkException(f'Failed after {retries} attempts: {e}')
            time.sleep(delay)

def process_data(url):
    try:
        data = request_with_retry(url)
        # Process your data here
        return data
    except NetworkException as e:
        print(e)
        return None
