from django.db import models

# Create your models here.

class ToDolist(models.Model):
    text = models.CharField(max_length=45)
    completed = models.BooleanField(default=False)