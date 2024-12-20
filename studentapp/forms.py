from django import forms
from .models import TodoList, Blog, NoteUpload

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['text']  # Include the fields you want in the form
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type your task...'}),
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']  # Include the fields you want in the form
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter blog title...'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your blog content here...'}),
        }

class NoteUploadForm(forms.ModelForm):
    class Meta:
        model = NoteUpload
        fields = ['title', 'file']  # Include the fields you want in the form
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter note title...'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }