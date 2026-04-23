import time
import random
import requests

def retry_request(url, max_retries=5, backoff_factor=0.3):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an error for bad responses
            return response.json()  # Assuming the response is JSON
        except requests.exceptions.RequestException as e:
            retries += 1
            wait_time = backoff_factor * (2 ** retries) + random.uniform(0, 1)
            print(f'Attempt {retries} failed: {e}. Retrying in {wait_time:.2f} seconds...')
            time.sleep(wait_time)
    return None  # Return None after max retries

# Example usage
if __name__ == '__main__':
    result = retry_request('https://api.example.com/data')
    print(result)  # Handle the response accordingly