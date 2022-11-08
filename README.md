# django-music-library
*Тестовое задание в Палиндром*
> [**Swagger**](https://app.swaggerhub.com/apis/stkudryashov/music-library-api/1.0.0)

## Инструкция по запуску
* Создать и заполнить **_.env_** файл в директории **_django-music-library_**
```
SECRET_KEY=your_django_secret_key
CSRF_TRUSTED_ORIGINS=http://127.0.0.1

POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=database_name

DB_HOST=database
DB_PORT=5432
```

* Выполнить `docker-compose up --build -d`
```
http://127.0.0.1:80
```
