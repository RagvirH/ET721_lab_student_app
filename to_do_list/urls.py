# to_do_list/urls.py
from django.urls import path
from . import views

app_name = 'to_do_list'  # This line is important for namespacing

urlpatterns = [
    path("", views.index, name='index'),
    path('add/', views.add_task, name='add'),  # Ensure this matches your view function
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('delete-completed/', views.delete_all_completed, name='delete_completed'),
]
