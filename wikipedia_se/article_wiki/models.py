from django.db import models

# Create your models here.

class article(models.Model):
    title = models.CharField(max_length=100)
    article = models.TextField()