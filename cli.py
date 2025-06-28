from core import fetch_weather
from colorama import Fore, init
from config import DEFAULT_UNITS, APP_NAME, APP_VERSION
import os

# Initialize colorama for colored terminal output
init(autoreset=True)

def clear_screen():
    """Clear the terminal screen for better readability."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_welcome():
    """Display a welcome message."""
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + f"          {APP_NAME} v{APP_VERSION}")
    print(Fore.CYAN + "=" * 50)

def run_cli():
    """Main CLI interface for the weather application."""
    clear_screen()
    display_welcome()
    
    # Use default units from config (user can change later)
    units = DEFAULT_UNITS
    symbol = "°C" if units == "metric" else "°F"
    last_location = None


    while True:
        # Display command options
        print(f"\n{Fore.WHITE}Current Units: {Fore.YELLOW}{units.capitalize()} ({symbol})")
        print("\nCommands:")
        print("  1 - Enter location")
        print("        - City/City, State")
        print("        - Zip Code")
        print("        - Coordinates (Lat, Lon)")
        print("  2 - Change units")
        if last_location:
            print(f"  3 - Check {last_location.upper()} again")
            print("  4 - Help")
            print("  5 - Exit")
        else:
            print("  3 - Help")
            print("  4 - Exit")
        inp = input("Selection: ").strip()

        # Handle exit command
        exit_choice = "5" if last_location else "4"
        if inp == exit_choice:
            # Exit the application
            print(Fore.BLUE + "Goodbye!")
            break
        elif inp == "2":
            # Change unit system
            units = get_unit_selection()
            symbol = "°C" if units == "metric" else "°F"
            continue
        elif inp == "3" and last_location:
            # Use last location
            location = last_location
        elif inp == "4" and last_location:
            # Show help
            display_help()
            continue
        elif inp == "3" and not last_location:
            # Show help
            display_help()
            continue
        elif inp == "1":
            # Prompt user to enter location
            while True:
                location = input("Enter City, Zip, or Coordinates: ").strip()
                if not location:
                    print(Fore.RED + "Please enter a valid location.")
                    continue
                
                # Validate location format
                is_valid, error_msg = is_valid_location_format(location)
                if is_valid:
                    break
                print(Fore.RED + f"Invalid input: {error_msg}")
        else:
            # Treat input as location directly
            location = inp.strip()
            if not location:
                print(Fore.RED + "Please enter a valid location.")
                continue
            
            # Validate location format for direct input too
            is_valid, error_msg = is_valid_location_format(location)
            if not is_valid:
                print(Fore.RED + f"Invalid input: {error_msg}")
                print(Fore.YELLOW + "Please use menu option 1 to enter a location, or try again.")
                continue

        # Normalize location for state abbreviations
        location = normalize_location(location)

        # Validate location format before API call
        is_valid, error_message = is_valid_location_format(location)
        if not is_valid:
            print(Fore.RED + f"ERROR: {error_message}")
            continue

        try:
            # Fetch weather data for the given location and units
            data = fetch_weather(location, units)
            
            # Store this as the last successful location
            last_location = location
            
            # Extract weather data with safe defaults
            desc = data.get("weather", [{}])[0].get("description", "N/A")
            temp = data.get("main", {}).get("temp", 0)
            feels_like = data.get("main", {}).get("feels_like", 0)
            humidity = data.get("main", {}).get("humidity", 0)
            pressure = data.get("main", {}).get("pressure", 0)
            wind = data.get("wind", {}).get("speed", 0)
            visibility = data.get("visibility", 0) / 1000 if data.get("visibility") else None  # Convert to km
            name = data.get("name", location)

            # Display weather information with colors
            print(Fore.CYAN + f"\n{'='*40}")
            print(Fore.LIGHTBLUE_EX + f"Weather for {name}")
            print(Fore.CYAN + f"{'='*40}")
            print(Fore.YELLOW + f"Condition: {desc.capitalize()}")
            print(Fore.LIGHTRED_EX + f"Temperature: {temp:.1f}{symbol}")
            print(Fore.MAGENTA + f"Feels like: {feels_like:.1f}{symbol}")
            print(Fore.RED + f"Humidity: {humidity}%")
            print(Fore.BLUE + f"Pressure: {pressure} hPa")
            wind_unit = "mph" if units == "imperial" else "m/s"
            print(Fore.GREEN + f"Wind: {wind} {wind_unit}")
            if visibility:
                distance_unit = "miles" if units == "imperial" else "km"
                vis_value = visibility * 0.621371 if units == "imperial" else visibility
                print(Fore.WHITE + f"Visibility: {vis_value:.1f} {distance_unit}")
            print(Fore.CYAN + f"{'='*40}")

        except Exception as e:
            # Handle errors (e.g., invalid location, network issues)
            print(Fore.RED + f"ERROR: {e}")

def get_unit_selection():
    """Prompt user to select metric or imperial units."""
    while True:
        print(f"\n{Fore.YELLOW}Select Unit System:")
        print("1. Metric (Celsius, m/s, km)")
        print("2. Imperial (Fahrenheit, mph, miles)")
        choice = input("Choice: ").strip()
        if choice == "1":
            return "metric"
        elif choice == "2":
            return "imperial"
        print(Fore.RED + "Invalid choice. Please select 1 or 2.")

def normalize_location(location: str) -> str:
    """
    If the user enters city,state_abbr, automatically append ',US' for OpenWeather API.
    Also validates coordinate format.
    """
    location = location.strip()
    if not location:
        return location
        
    # Check if it looks like coordinates
    if "," in location and not any(char.isalpha() for char in location):
        try:
            parts = location.split(",")
            if len(parts) == 2:
                lat, lon = map(float, parts)
                if -90 <= lat <= 90 and -180 <= lon <= 180:
                    return f"{lat},{lon}"
                else:
                    raise ValueError("Coordinates out of valid range")
        except ValueError:
            pass  # Will be handled as regular location
    
    # Handle city,state format
    parts = [p.strip() for p in location.split(",")]
    if len(parts) == 2 and len(parts[1]) == 2 and parts[1].isalpha():
        # Looks like city,state_abbr
        return f"{parts[0]},{parts[1].upper()},US"
    return location


def is_valid_location_format(location: str) -> tuple[bool, str]:
    """
    Validate if the location input is not empty.
    
    Returns:
        tuple: (is_valid, error_message)
    """
    location = location.strip()
    
    # Check for empty input
    if not location:
        return False, "Location cannot be empty."
    
    return True, ""

def display_help():
    """Display help information for the weather app."""
    print(f"\n{Fore.CYAN}HELP - Weather App Usage")
    print(f"{Fore.CYAN}{'='*30}")
    print(f"{Fore.YELLOW}Location Formats - case insensitive:")
    print("  • City name: 'New York' or 'London'")
    print("  • City, State: 'Miami, FL' (US states)")
    print("  • City, Country: 'Paris, FR'")
    print("  • ZIP code: '10001' (US only)")
    print("  • Coordinates: '40.7128,-74.0060' (lat,lon)")
    print(f"\n{Fore.YELLOW}Tips:")
    print("  • Use option 3 to quickly recheck your last location")
    print("  • API requires WEATHER_API_KEY environment variable")
    print("  • Get your free API key from openweathermap.org")
    print(f"{Fore.CYAN}{'='*30}")
