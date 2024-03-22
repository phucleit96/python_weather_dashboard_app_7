# Importing necessary libraries
import pandas as pd
import os
import requests

# API Key for OpenWeatherMap API

# Alternative way to get API Key from environment variables
API_KEY = os.getenv("OPEN_WEATHER_API_KEY")

# Function to get weather data
def get_data(place, forecast_days=None):
    # Constructing the URL for the API request
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    # Making a GET request to the API
    response = requests.get(url)
    # Converting the response to JSON
    data = response.json()
    # Filtering the data for the required number of forecast days
    filtered_data = data['list'][:8*forecast_days]
    # Returning the filtered data
    return filtered_data

# Main execution
if __name__ == "__main__":
    # Printing the weather data for Tokyo for the next 3 days
    print(get_data(place="Tokyo", forecast_days=3))