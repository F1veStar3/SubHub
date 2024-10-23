import os
import time

from celery import Celery

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service.settings')

app = Celery('service')
app.config_from_object('django.conf.settings')
app.conf.broker_url = settings.CELERY_BROKEN_URL
app.autodiscover_tasks()


@app.task()
def debug_task():
    time.sleep(5)
    print('Hello from debug_task)))')

