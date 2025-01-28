from typing import Optional

import requests
import json
from requests.exceptions import RequestException


class WeatherServiceError(Exception):
    """Custom exception for errors in the WeatherService class."""

    pass


def get_weather(city: str, api_key: Optional[str] = None) -> Optional[float]:
    """
    Fetches the current temperature for a given city from the weather API.

    Args:
        city (str): The city for which to retrieve the weather data.
        api_key (Optional[str]): The API key for authentication. If not provided, uses a default.

    Returns:
        Optional[float]: The current temperature if the data is available, otherwise None.

    Raises:
        WeatherServiceError: If there is an issue with the API request or the response is invalid.
    """
    if api_key is None:
        api_key = "your_default_api_key"  # Replace with a real default key or configure it externally

    url = f"https://api.weather.com/v3/weather/conditions?city={city}&apikey={api_key}"

    try:
        response = requests.get(url, timeout=5)  # Timeout to avoid hanging requests
        if response.status_code != 200:
            raise WeatherServiceError(f"Failed to fetch weather data for {city}")
    except RequestException as e:
        raise WeatherServiceError(f"Failed to fetch weather data for {city}") from e

    try:
        temperature = response.json().get("temperature")
        if temperature is None:
            raise WeatherServiceError("Temperature data is missing in the response")
        return temperature
    except AttributeError as e:
        raise WeatherServiceError("Failed to parse weather data") from e
