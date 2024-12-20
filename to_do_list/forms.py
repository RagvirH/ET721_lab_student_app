from django import forms
from .models import TodoList

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['text', 'completed']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
