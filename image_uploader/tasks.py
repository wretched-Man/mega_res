import uuid
from celery import shared_task
from . import forms
from . import models
from ai_model.process_image import process
import time
@shared_task()
def run_inference(data):
    instance = models.UserUpload()
    try:
        result = process(data)
        instance.image.save(str(uuid.uuid4()) + ".png", result)
        instance.save()
    except:
        return {"error" : "An error Occured"}
    return {"image_url" : instance.image.url}