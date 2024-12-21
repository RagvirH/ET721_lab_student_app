from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import NoteImage
from .forms import NoteImageForm

class NotesListView(ListView):
    model = NoteImage
    template_name = 'upload_notes/notes_list.html'
    context_object_name = 'object_list'

class NotesUploadView(CreateView):
    model = NoteImage
    form_class = NoteImageForm
    template_name = 'upload_notes/notes_upload.html'
    success_url = reverse_lazy('notes_list')