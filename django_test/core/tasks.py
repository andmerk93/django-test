from django.core.mail import send_mail

from django.conf import settings

from django_test.celery import app

from .views import import_weather


@app.task
def import_place_by_task(place_name, author_id):
    serializer = import_weather(place_name, author_id)
    if serializer.is_valid():
        serializer.save()
        return f'{place_name} weather was saved'
    return f'{place_name} weather was not saved'


@app.task
def send_mail_by_task(
    subject,
    message,
    emails,
):
    send_mail(
        subject,
        message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=emails,
    )
