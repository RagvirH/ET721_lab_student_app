from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

def get_default_user():
    return User.objects.first().id if User.objects.exists() else None

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default='')
    file = models.FileField(upload_to='posts/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)  # Changed this line
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)

    def __str__(self):
        return self.title
