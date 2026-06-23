import requests
from unittest.mock import patch, MagicMock

from weather_reporter import (
    get_current_weather,
    get_weather_summary,
    format_weather_report,
)

@patch("weather_reporter.requests.get")
def test_get_current_weather_success(mock_get):
    response = MagicMock()
    response.status_code = 200
    response.json.return_value = {
        "name": "London",
        "main": {"temp": 20, "humidity": 65},
        "weather": [{"description": "clear sky"}],
        "wind": {"speed": 3.5},
    }
    mock_get.return_value = response

    result = get_current_weather("London")
    assert result["city"] == "London"
    assert result["temp_c"] == 20

@patch("weather_reporter.requests.get")
def test_get_current_weather_error(mock_get):
    response = MagicMock()
    response.status_code = 404
    mock_get.return_value = response

    assert get_current_weather("BadCity") is None

def test_empty_city():
    import pytest
    with pytest.raises(ValueError):
        get_current_weather("")

def test_format_weather_report():
    weather = {
        "temp_c": 18,
        "description": "clear sky",
        "humidity": 60,
        "wind_speed": 2.5,
    }
    report = format_weather_report("Paris", weather)
    assert "Paris" in report

@patch("weather_reporter.requests.get")
def test_summary_multiple_cities(mock_get):
    response = MagicMock()
    response.status_code = 200
    response.json.return_value = {
        "name": "London",
        "main": {"temp": 20, "humidity": 60},
        "weather": [{"description": "clear"}],
        "wind": {"speed": 1.0},
    }
    mock_get.return_value = response

    result = get_weather_summary(["London", "Paris"])
    assert len(result) == 2

@patch("weather_reporter.requests.get")
def test_side_effect_success_and_failure(mock_get):
    ok = MagicMock()
    ok.status_code = 200
    ok.json.return_value = {
        "name": "London",
        "main": {"temp": 20, "humidity": 60},
        "weather": [{"description": "clear"}],
        "wind": {"speed": 1.0},
    }

    bad = MagicMock()
    bad.status_code = 404

    mock_get.side_effect = [ok, bad]

    result = get_weather_summary(["London", "BadCity"])

    assert result["London"] is not None
    assert result["BadCity"] is None

@patch("weather_reporter.requests.get")
def test_timeout_handled(mock_get):
    mock_get.side_effect = requests.exceptions.Timeout()

    result = get_weather_summary(["London"])

    assert result["London"] is None

@patch("weather_reporter.requests.get")
def test_integration_pipeline(mock_get):
    response = MagicMock()
    response.status_code = 200
    response.json.return_value = {
        "name": "London",
        "main": {"temp": 22, "humidity": 50},
        "weather": [{"description": "sunny"}],
        "wind": {"speed": 4.0},
    }

    mock_get.return_value = response

    weather = get_current_weather("London")
    report = format_weather_report("London", weather)

    assert "London" in report
    assert "22" in report
