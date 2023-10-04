from django.db import models
from django.contrib.auth.models import User
import os

class item(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    def content_file_name(instance, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (instance.name, ext)
        return os.path.join('images', filename)
    image = models.ImageField(upload_to=content_file_name)  

