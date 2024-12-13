from django.db import models

# Create your models here.


class Record(models.Model):
    regex = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    result = models.BooleanField()
