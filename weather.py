from datetime import datetime, timedelta

import requests

from constant import WEATHER_URL, DAYS, WEATHER_CODE
from models import WeatherDetail, WeatherResponse


def get_weather(city: str):
    """
    Получение координат через API
    (Тут мы получаем координаты, через ввод города).
    Далее данные координаты прокидываются в другое API
    с получением прогноза погоды через координаты.
    Потом мы получаем ответ json, забираем и прогоняем через их через цикл.
    """
    geocode_url = (f"https://geocoding-api.open-meteo.com/v1/search?"
                   f"name={city}&count=1&language=ru&format=json")
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
