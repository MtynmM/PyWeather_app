import os
from typing import Optional
import requests
from dotenv import load_dotenv

load_dotenv()


class WeatherService:

    _BASE_URL = "http://api.weatherapi.com/v1/current.json"
    _API_KEY = os.getenv("WEATHER_API_KEY")
    _DEFAULT_LOCATION = "Isfahan"

    def get_weather(self, location: Optional[str]) -> Optional[dict]:
        if not location or not location.strip():
            location = self._DEFAULT_LOCATION

        params = {
            "key": self._API_KEY,
            "q": location,
        }

        try:
            response = requests.get(self._BASE_URL, params=params)
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return None
        return response.json()
