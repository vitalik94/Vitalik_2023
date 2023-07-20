from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    genre = models.CharField(max_length=100)
    image = models.FileField(upload_to='img/')
    description = models.TextField()
