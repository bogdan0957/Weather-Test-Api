import requests

from constant import WEATHER_URL, DAYS, WEATHER_CODE
from models import WeatherDetail, WeatherResponse
from datetime import datetime, timedelta


def get_weather(city: str):
    geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=ru&format=json"
    geocode_response = requests.get(geocode_url).json()
    cord = geocode_response["results"][0]
    lat = cord['latitude']
    long = cord['longitude']
    response = requests.get(
        WEATHER_URL, params={
            "latitude": lat,
            "longitude": long,
            "daily": ["temperature_2m_max", 'weather_code'],
            "timezone": "UTC"
        }
    ).json()
    daily_data = response.get("daily")
    forecast = []
    start_date = datetime.now()
    for i in range(DAYS):
        date = start_date + timedelta(days=i)
        temperature = daily_data["temperature_2m_max"][i]
        weather_code = daily_data["weather_code"][i]
        code = WEATHER_CODE[weather_code]

        weather_item = WeatherDetail(
            date=date.isoformat(),
            temperature=temperature,
            weather_description=code
        )
        forecast.append(weather_item)

    return WeatherResponse(city=city, forecast=forecast)


print(get_weather('Ижевск'))
