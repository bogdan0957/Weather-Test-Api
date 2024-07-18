from typing import List

from pydantic import BaseModel


class WeatherDetail(BaseModel):
    """Модель погоды"""
    date: str
    temperature: float
    weather_description: str


class WeatherResponse(BaseModel):
    """Модель ответа API"""
    city: str
    forecast: List[WeatherDetail]
