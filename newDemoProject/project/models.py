from django.db import models

# Create your models here.

class College(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    link = models.TextField(null=False, blank=False)
