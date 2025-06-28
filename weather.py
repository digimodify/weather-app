import argparse
from cli import run_cli

def main():
    # Create an argument parser for command-line options
    parser = argparse.ArgumentParser(description="Weather App")
  
    args = parser.parse_args()

    # Run the CLI interface
    run_cli()

# Entry point of the script
if __name__ == "__main__":
    main()
