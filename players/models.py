from django.db import models

# Create your models here.


class Players(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    comment = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
