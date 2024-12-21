from django.db import models

class NoteImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='notes/')  # Save images in 'media/notes/'

    def __str__(self):
        return self.title