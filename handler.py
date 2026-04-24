from typing import Any, Dict, List, Optional

class RobloxHandler:
    def __init__(self, api_key: str, base_url: str) -> None:
        """
        Initializes the RobloxHandler with API key and base URL.
        
        :param api_key: The API key for authentication.
        :param base_url: The base URL for the Roblox API.
        """
        self.api_key = api_key
        self.base_url = base_url

    def fetch_data(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Fetches data from the given API endpoint.
        
        :param endpoint: The API endpoint to fetch data from.
        :param params: Optional dictionary of query parameters.
        :return: Parsed JSON response from the API.
        """
        import requests
        response = requests.get(f"{self.base_url}/{endpoint}", params=params, headers={"Authorization": f"Bearer {self.api_key}"})
        response.raise_for_status()
        return response.json()

    def process_result(self, data: Dict[str, Any]) -> List[str]:
        """
        Processes the fetched data and returns a list of results.
        
        :param data: The data dictionary to process.
        :return: List of processed result strings.
        """
        return [f"Result: {item['name']} (ID: {item['id']})" for item in data.get('results', [])]

    def handle_request(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> List[str]:
        """
        Handles the entire request process and returns the results.
        
        :param endpoint: The API endpoint to hit.
        :param params: Optional parameters for the request.
        :return: List of processed results.
        """
        data = self.fetch_data(endpoint, params)
        results = self.process_result(data)
        return results
