from django import forms
from . import models

class UploadImage(forms.ModelForm):
    class Meta:
        model = models.UserUpload
        fields = ["image"]