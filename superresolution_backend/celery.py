import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "superresolution_backend.settings")
app = Celery("superresolution_backend")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()