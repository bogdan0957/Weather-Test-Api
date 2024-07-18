from pydantic import BaseModel


class Weather(BaseModel):
    """Модель погоды с передачей параметра city."""
    city: str
