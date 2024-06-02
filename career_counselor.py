import requests
from tenacity import retry, wait_exponential, stop_after_attempt
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CareerCounselor:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.geminipro.com/v1"

    @retry(wait=wait_exponential(multiplier=1, min=4, max=10), stop=stop_after_attempt(3))
    def get_career_advice(self, field):
        endpoint = f"{self.base_url}/career_advice"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "field": field
        }
        try:
            response = requests.post(endpoint, json=data, headers=headers)
            response.raise_for_status()  # Raises HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error getting career advice: {e}")
            raise

    @retry(wait=wait_exponential(multiplier=1, min=4, max=10), stop=stop_after_attempt(3))
    def get_roadmap(self, field):
        endpoint = f"{self.base_url}/roadmap"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "field": field
        }
        try:
            response = requests.post(endpoint, json=data, headers=headers)
            response.raise_for_status()  # Raises HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error getting roadmap: {e}")
            raise