from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from router import router as router_pages
from schemas import Weather
from weather import get_weather

app = FastAPI()

app.include_router(router_pages)


@app.post("/weather")
async def weather(request: Weather):
    """Основная функция"""
    try:
        weather_data = get_weather(request.city)
        return weather_data
    except Exception:
        raise HTTPException(status_code=400, detail={
            'Not Ok'
        })


origins = [
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie",
                   "Access-Control-Allow-Headers",
                   "Access-Control-Allow-Origin",
                   "Authorization"],
)
