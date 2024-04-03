from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Task(MPTTModel):
    name = models.CharField(max_length=50)
    completion = models.PositiveSmallIntegerField()
    description = models.TextField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    supervisor = models.CharField(max_length=50)
    executor = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
