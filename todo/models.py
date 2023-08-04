from django.db import models

# Create your models here.


class TodoModel(models.Model):
    subject = models.CharField(max_length=30)
    details = models.TextField(max_length=300)