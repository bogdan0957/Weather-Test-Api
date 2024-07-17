from pydantic import BaseModel


class Weather(BaseModel):
    city: str

