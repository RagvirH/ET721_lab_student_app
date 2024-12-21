from django.urls import path
from .views import NotesListView, NotesUploadView

urlpatterns = [
    path('', NotesListView.as_view(), name='notes_list'),
    path('upload/', NotesUploadView.as_view(), name='notes_upload'),
]