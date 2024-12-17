from django.shortcuts import render, HttpResponse
from . import forms
from .tasks import run_inference
from celery.result import AsyncResult
import json

# Create your views here.
# Welcome page
def home_view(request, *args, **kwargs):
    default_form = forms.UploadImage()
    if request.method == 'GET':
        return render(request, "index.html", {"form" : default_form})

# Upload page
def upload_view(request, *args, **kwargs):
    default_form = forms.UploadImage()
    if request.method == 'POST':
        if request.FILES.get("image", None) is None:
            return render(request, "index.html", {"form" : default_form})

        image = request.FILES['image'].read()
        inference_result = run_inference.delay(image)
        return render(request, "result.html", {"task_id" : inference_result.id})
    

def get_status(request, task_id):
    task = AsyncResult(task_id)
    return HttpResponse(
        json.dumps({
            "status" : task.status,
            "result" : task.result
        })
    )