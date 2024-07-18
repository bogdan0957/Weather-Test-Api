from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from weather import get_weather

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)


@router.get("/base")
def get_base_page(request: Request):
    """Отрисовка базовой страницы."""
    return templates.TemplateResponse("base.html", {"request": request})


@router.get("/weather/{city}")
def get_weather_page(request: Request, weather_city=Depends(get_weather)):
    """Отрисовка страницы с прогнозом погоды для определенного города."""
    return templates.TemplateResponse("weather.html", {
        "request": request, "weather_city": weather_city
    })
