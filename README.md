# django-test

### Запуск

Для запуска нужно создать в корневой директории `.env` вида

```
SECRET_KEY="django-insecure-secret-key"
OWM_API_KEY=API10005000500205
DJANGO_DEBUG=True
```

Установка и запуск стандартно (из виртуального окружения):

```
python -m venv venv
.\venv\Scripts\activate    (win)
source .\venv\bin\activate (linux)
pip install -r requirements.txt
python .\django_test\manage.py migrate
python .\django_test\manage.py runserver 80
```

Тестовый сервер поднимется и будет доступен по http://localhost/


Для создания суперюзера нужно выполнить из вирт. окружения

```
python .\django_test\manage.py createsuperuser
```



### TODO:
- easy_thumbnails / https://github.com/dessibelle/sorl-thumbnail-serializer-field
- импорт мест из xlsx
- экспорт погоды в xlsx
- логины и пермишены
- readme
- docker