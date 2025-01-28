import pytest  # type: ignore
from requests.exceptions import RequestException

from src.weather_service import WeatherServiceError, get_weather


def test_get_weather_success(mocker):
    """
    Test that get_weather returns the correct temperature when the API call succeeds.
    """
    mocker.patch(
        "requests.get",
        return_value=mocker.MagicMock(
            status_code=200, json=lambda: {"temperature": 22}
        ),
    )

    result = get_weather("New York", api_key="test_api_key")
    assert result == 22


def test_get_weather_none_temperature(mocker):
    """
    Test that get_weather raises WeatherServiceError if the temperature is None.
    """
    mocker.patch(
        "requests.get",
        return_value=mocker.MagicMock(
            status_code=200, json=lambda: {"temperature": None}
        ),
    )

    with pytest.raises(
        WeatherServiceError, match="Temperature data is missing in the response"
    ):
        get_weather("New York", api_key="test_api_key")


def test_get_weather_failure(mocker):
    """
    Test that get_weather raises WeatherServiceError when the API call fails.
    """

    mocker.patch(
        "requests.get",
        return_value=mocker.MagicMock(
            status_code=404, json=lambda: {"temperature": None}
        ),
    )

    with pytest.raises(
        WeatherServiceError, match="Failed to fetch weather data for NonExistentCity"
    ):
        get_weather("NonExistentCity", api_key="test_api_key")


def test_get_weather_missing_temperature(mocker):
    """
    Test that get_weather raises WeatherServiceError if temperature is missing in the response.
    """

    mocker.patch(
        "requests.get",
        return_value=mocker.MagicMock(status_code=200, json=lambda: {}),
    )
    with pytest.raises(
        WeatherServiceError, match="Temperature data is missing in the response"
    ):
        get_weather("New York", api_key="test_api_key")


def test_get_weather_json_parsing_error(mocker):
    """
    Test that get_weather raises WeatherServiceError if JSON parsing fails.
    """
    mocker.patch(
        "requests.get",
        return_value=mocker.MagicMock(status_code=200, json=lambda: "Invalid Json"),
    )

    with pytest.raises(WeatherServiceError, match="Failed to parse weather data"):
        get_weather("New York", api_key="test_api_key")


def test_get_weather_request_exception(mocker):
    """
    Test that get_weather raises WeatherServiceError if a request exception occurs.
    """
    mock_get = mocker.patch("requests.get")
    mock_get.side_effect = RequestException("Network error")

    with pytest.raises(
        WeatherServiceError, match="Failed to fetch weather data for New York"
    ):
        get_weather("New York", api_key="test_api_key")
