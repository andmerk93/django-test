from datetime import timedelta
import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_test.settings")
app = Celery("django_test")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = dict(
    import_place_beat=dict(
        task='core.tasks.import_place_by_task',
        schedule=timedelta(seconds=10),
#        schedule=crontab(minute='*/1'),
        args=('krai', 1)
    ),
)
