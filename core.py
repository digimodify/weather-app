import os
import requests
from config import DEFAULT_TIMEOUT

GEOCODE_API = "https://api.openweathermap.org/geo/1.0/direct"
WEATHER_API = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(location, units):
    """
    Fetch weather data from OpenWeatherMap API.
    
    Args:
        location (str): Location query (city, zip, coordinates)
        units (str): Unit system ('metric' or 'imperial')
        
    Returns:
        dict: Weather data from API
        
    Raises:
        ValueError: For invalid API key or location
        ConnectionError: For network-related issues
    """
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        raise ValueError("API key missing. Please set WEATHER_API_KEY environment variable.")

    params = {"appid": api_key, "units": units}

    # Parse location input
    if "," in location and not any(char.isalpha() for char in location):
        try:
            lat, lon = map(float, location.split(","))
            if -90 <= lat <= 90 and -180 <= lon <= 180:
                params["lat"], params["lon"] = lat, lon
            else:
                raise ValueError("Coordinates must be between -90/90 for latitude and -180/180 for longitude")
        except ValueError as e:
            if "Coordinates must be" in str(e):
                raise e
            params["q"] = location
    elif location.isdigit() and len(location) == 5:
        params["zip"] = f"{location},US"
    else:
        params["q"] = location

    try:
        response = requests.get(WEATHER_API, params=params, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
        
        data = response.json()
        if data.get("cod") == "404":
            raise ValueError(f"Location '{location}' not found. Please check spelling and try again.")
        
        return data
    except requests.exceptions.Timeout:
        raise ConnectionError("Request timed out. Please check your internet connection.")
    except requests.exceptions.ConnectionError:
        raise ConnectionError("Unable to connect to weather service. Please check your internet connection.")
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            raise ValueError("Invalid API key. Please check your WEATHER_API_KEY.")
        raise ConnectionError(f"Weather service error: {e}")
