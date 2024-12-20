from django.db import models

class TodoList(models.Model):  # Make sure it's TodoList, not ToDoList or ToDolist
    text = models.CharField(max_length=45)
    completed = models.BooleanField(default=False)
