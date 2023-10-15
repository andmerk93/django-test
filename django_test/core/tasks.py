from django.core.mail import send_mail

from django.conf import settings

from django_test.celery import app

from .views import import_weather


@app.task
def import_place_by_task(place_name, author_id=settings.CELERY_USER_ID):
    serializer = import_weather(place_name, author_id)
    if serializer.is_valid():
        serializer.save()


@app.task
def send_mail_by_task(emails):
#    return (str(type(emails)), emails)
    send_mail(
        subject='subj',
        message='msg',
        recipient_list=emails,
        from_email=settings.DEFAULT_FROM_EMAIL,
    )
