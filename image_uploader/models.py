from django.db import models

# Create your models here.
class UserUpload(models.Model):
    image = models.ImageField(upload_to="uploads/")

    def delete(self, *args, **kwargs):
        # Delete image and video
        self.image.delete()
        super(UserUpload, self).delete(*args, **kwargs)