from fastapi import FastAPI, HTTPException
from weather import get_weather
from schemas import Weather

app = FastAPI()


@app.post("/weather")
async def weather(request: Weather):
    try:
        weather_data = get_weather(request.city)
        return weather_data
    except Exception:
        raise HTTPException(status_code=400, detail={
            'Not Ok'
        })




