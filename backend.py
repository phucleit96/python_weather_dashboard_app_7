import pandas as pd
import os
import requests

API_KEY = 'b5b2f64dd6cc91df4fd94eef842ca6e6'
# API_KEY = os.getenv("OPEN_WEATHER_API_KEY")


def get_data(place, forecast_days=None, kind=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list'][:8*forecast_days]
    if kind == "Temperature":
        filtered_data = [dict['main']['temp'] for dict in filtered_data]
    else:
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind="Temperature"))
