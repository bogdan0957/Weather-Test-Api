# Weather forecast
### Добрый день, меня зовут Богдан. Я сделал приложение для получения прогноз погоды по городу.
### Стек технологий: 
- Fastapi
- requests
- pytest
- docker
## Установка
1. Клонирование репозитория 
```git clone https://github.com/bogdan0957/Weather-Test-Api.git```
2. Переход в папку
   ```cd Weather-Test-API```
3. Сбилдить docker
   ```docker build -t "Ваше название" .```
4. Запуск docker контейнера
   ```docker run -d -p 8000:8000 Название вашего контейнера```
5. По ссылке ```localhost:8000/pages/Weather/"Название города"``` можно получить данные по прогнозу погоды
6. Далее по этой же ссылке есть поле для ввода другого города.
7. По ссылке ```locahost:8000/docs``` можно посмотреть документацию API с возможность самому протестировать API.