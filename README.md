![Weather App Banner](assets/banner.png)

# Weather App 🌤️

A simple, colorful command-line weather application that fetches real-time weather data using the OpenWeatherMap API.

## Features ✨

- **Real-time Weather Data**: Get current weather conditions for any location worldwide
- **Multiple Location Formats**: Support for cities, states, countries, ZIP codes, and coordinates
- **Unit System Selection**: Choose between Metric (Celsius) and Imperial (Fahrenheit) units
- **Colorful Display**: Beautiful colored output for better readability
- **Last Location Memory**: Quickly recheck your most recent location
- **Input Validation**: Basic input validation to prevent empty entries
- **Smart Location Parsing**: Automatic formatting for US cities (adds ",US" for state abbreviations)
- **Comprehensive Help**: Built-in help system with usage examples
- **Cross-platform**: Works on Windows, macOS, and Linux

## Screenshots 📸

```
==================================================
          WEATHER APP
==================================================

Starting with Imperial units by default. Use option 2 to change.

Current Units: Imperial (°F)

Commands:
  1 - Enter location
        - city/city,state
        - zip code
        - coordinates (lat,lon)
  2 - Change units
  3 - Help
  4 - Exit

========================================
Weather for New York
========================================
Condition: Clear sky
Temperature: 72.5°F
Feels like: 75.4°F
Humidity: 65%
Pressure: 1013 hPa
Wind: 7.2 mph
Visibility: 6.2 miles
========================================
```

## Installation 🚀

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Setup

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd weather_app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Get an API Key**
   - Visit [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up for a free account
   - Navigate to the "API keys" section
   - Copy your API key

4. **Set up your API Key**
   
   **Option 1: Environment Variable (Recommended)**
   
   - **Windows Command Prompt:**
     ```cmd
     set WEATHER_API_KEY=your_api_key_here
     ```
   
   - **Windows PowerShell:**
     ```powershell
     $env:WEATHER_API_KEY='your_api_key_here'
     ```
   
   - **macOS/Linux:**
     ```bash
     export WEATHER_API_KEY=your_api_key_here
     ```
   
   **Option 2: Add to your shell profile (Permanent)**
   
   Add the export command to your shell profile file:
   - **Bash**: `~/.bashrc` or `~/.bash_profile`
   - **Zsh**: `~/.zshrc`
   - **Fish**: `~/.config/fish/config.fish`

## Usage 🎯

### Running the Application

```bash
python weather.py
```

### Location Input Formats

The app supports various location input formats (case insensitive):

| Format | Example | Description |
|--------|---------|-------------|
| City name | `London` | Simple city name |
| City, Country | `Paris, FR` | City with country code |
| City, State | `Miami, FL` | US city with state abbreviation |
| ZIP Code | `10001` | US ZIP code (5 digits) |
| Coordinates | `40.7128,-74.0060` | Latitude, Longitude |

### Menu Options

- **1 - Enter location**: Input a new location to check weather
- **2 - Change units**: Switch between Metric and Imperial units
- **3 - Check [location] again**: Quickly recheck your last searched location (when available)
- **3/4 - Help**: Display comprehensive help information
- **4/5 - Exit**: Close the application

*Note: Menu numbers adjust based on whether you have a previous location*

### Unit Systems

- **Metric**: Temperature in Celsius, wind speed in m/s, distances in km
- **Imperial**: Temperature in Fahrenheit, wind speed in mph, distances in miles

## Project Structure 📁

```
weather_app/
├── weather.py          # Main entry point
├── cli.py              # Command-line interface logic
├── core.py             # Weather API interaction
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── assets/
    └── banner.png     # App banner/logo
```

## Dependencies 📦

- **requests**: HTTP library for API calls
- **colorama**: Cross-platform colored terminal output

Install with:
```bash
pip install requests colorama
```

## Configuration ⚙️

The app includes a `config.py` file for customization:

```python
# Default settings
DEFAULT_UNITS = "imperial"        # Default unit system
DEFAULT_TIMEOUT = 10              # API request timeout
APP_NAME = "Weather App"          # Application name
APP_VERSION = "1.1"               # Version number

# Display settings
SHOW_DETAILED_WEATHER = True      # Show additional weather details
CLEAR_SCREEN_BETWEEN_QUERIES = False  # Clear screen between queries

# API settings
MAX_RETRIES = 3                   # Maximum API retry attempts
```

**Note**: The app now uses these config settings! It starts with Imperial units by default, and you can change the default by editing `config.py`.

## Error Handling 🛠️

The app handles various error conditions gracefully:

- **Invalid API Key**: Clear error message with setup instructions
- **Location Not Found**: Helpful suggestions for correct location format
- **Network Issues**: Timeout and connection error handling
- **Invalid Input**: Input validation prevents empty entries; other invalid locations are handled by API error messages

## Troubleshooting 🔧

### Common Issues

1. **"API key missing" error**
   - Ensure `WEATHER_API_KEY` environment variable is set
   - Restart your terminal/command prompt after setting the variable
   - Verify your API key is correct and active

2. **"Location not found" error**
   - Check spelling of city/location name
   - Try different location formats (e.g., add country code)
   - For US locations, try using state abbreviation

3. **Connection errors**
   - Check your internet connection
   - Verify firewall isn't blocking the application
   - Try again after a few moments

4. **Import errors**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version is 3.6 or higher

### Getting Help

If you encounter issues:
1. Check the built-in help system in the menu
2. Verify your API key is valid at [OpenWeatherMap](https://openweathermap.org/)
3. Ensure all dependencies are properly installed

## API Information 🌐

This app uses the [OpenWeatherMap Current Weather Data API](https://openweathermap.org/current):

- **Free Tier**: 1,000 API calls per day
- **Rate Limit**: 60 calls per minute
- **Data Updates**: Every 10 minutes
- **Coverage**: Worldwide weather data

## Contributing 🤝

Contributions are welcome! Some ideas for improvements:

- Add weather forecasts (5-day, hourly)
- Save favorite locations
- Weather alerts and notifications
- GUI version using tkinter or PyQt
- Weather history and trends
- Multiple language support

## License 📄

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments 🙏

- [OpenWeatherMap](https://openweathermap.org/) for providing the weather API
- [Colorama](https://github.com/tartley/colorama) for cross-platform colored output
- [Requests](https://requests.readthedocs.io/) for HTTP functionality

## Version History 📋

- **v1.0** - Initial release

---
