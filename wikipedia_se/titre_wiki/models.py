from django.db import models

# Create your models here.

class article_titre(models.Model):
    title = models.CharField(max_length=100)
