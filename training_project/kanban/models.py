from django.db import models


class Task(models.Model):
    status = models.CharField(max_length=50)
    description = models.TextField()
    executor = models.CharField(max_length=50)
    Id = models.AutoField(primary_key=True)