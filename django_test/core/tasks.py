from django.conf import settings

from django_test.celery import app

from .views import import_weather


@app.task
def import_place_by_task(place_name, author_id=settings.CELERY_USER_ID):
    serializer = import_weather(place_name, author_id)
    if serializer.is_valid():
        serializer.save()

