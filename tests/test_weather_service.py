from unittest.mock import Mock, patch

import pytest  # type: ignore
from requests.exceptions import RequestException

from src.weather_service import WeatherServiceError, get_weather


@patch("src.weather_service.requests.get")
def test_get_weather_success(mock_get):
    """
    Test that get_weather returns the correct temperature when the API call succeeds.
    """
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"temperature": 22}
    mock_get.return_value = mock_response

    result = get_weather("New York", api_key="test_api_key")
    assert result == 22


@patch("src.weather_service.requests.get")
def test_get_weather_none_temperature(mock_get):
    """
    Test that get_weather raises WeatherServiceError if the temperature is None.
    """
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"temperature": None}
    mock_get.return_value = mock_response

    with pytest.raises(
        WeatherServiceError, match="Temperature data is missing in the response"
    ):
        get_weather("New York", api_key="test_api_key")


@patch("src.weather_service.requests.get")
def test_get_weather_failure(mock_get):
    """
    Test that get_weather raises WeatherServiceError when the API call fails.
    """
    mock_response = Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    with pytest.raises(
        WeatherServiceError, match="Failed to fetch weather data for NonExistentCity"
    ):
        get_weather("NonExistentCity", api_key="test_api_key")


@patch("src.weather_service.requests.get")
def test_get_weather_missing_temperature(mock_get):
    """
    Test that get_weather raises WeatherServiceError if temperature is missing in the response.
    """
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {}
    mock_get.return_value = mock_response

    with pytest.raises(
        WeatherServiceError, match="Temperature data is missing in the response"
    ):
        get_weather("New York", api_key="test_api_key")


@patch("src.weather_service.requests.get")
def test_get_weather_json_parsing_error(mock_get):
    """
    Test that get_weather raises WeatherServiceError if JSON parsing fails.
    """
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.side_effect = ValueError
    mock_get.return_value = mock_response

    with pytest.raises(WeatherServiceError, match="Failed to parse weather data"):
        get_weather("New York", api_key="test_api_key")


@patch("src.weather_service.requests.get")
def test_get_weather_request_exception(mock_get):
    """
    Test that get_weather raises WeatherServiceError if a request exception occurs.
    """
    mock_get.side_effect = RequestException("Network error")

    with pytest.raises(
        WeatherServiceError, match="Failed to fetch weather data for New York"
    ):
        get_weather("New York", api_key="test_api_key")
