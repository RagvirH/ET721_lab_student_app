from django import forms
from .models import NoteImage

class NoteImageForm(forms.ModelForm):
    class Meta:
        model = NoteImage
        fields = ['title', 'image']