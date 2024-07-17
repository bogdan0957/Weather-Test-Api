from typing import List

from pydantic import BaseModel


class WeatherDetail(BaseModel):
    date: str
    temperature: float
    weather_description: str


class WeatherResponse(BaseModel):
    city: str
    forecast: List[WeatherDetail]


