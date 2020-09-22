from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.dev')

app = Celery('{{ files.1 }}_celery', broker=settings.BROKER_URL)
app.config_from_object('celeryconfig')
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

if __name__ == '__main__':
    app.start()
