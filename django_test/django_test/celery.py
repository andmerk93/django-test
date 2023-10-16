from datetime import timedelta
import os

from celery import Celery

from constance import config as settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_test.settings")
app = Celery("django_test")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = dict(
    import_place_beat=dict(
        task='core.tasks.import_place_by_task',
        schedule=timedelta(minutes=settings.WEATHER_PERIOD),
        args=(
            settings.WEATHER_PLACE,
            settings.CELERY_USER_ID
        )
    ),
    send_mails_beat=dict(
        task='core.tasks.send_mail_by_task',
        schedule=timedelta(minutes=settings.MAIL_PERIOD),
        args=(
            settings.MAIL_SUBJECT,
            settings.MAIL_MESSAGE,
            settings.EMAILS_LIST,
        )
    )
)
