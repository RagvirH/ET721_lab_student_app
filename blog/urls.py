from django.urls import path
from .views import post_list, post_detail, post_create, post_edit

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:id>/', post_detail, name='post_detail'),
    path('new/', post_create, name='post_create'),
    path('<int:id>/edit/', post_edit, name='post_edit'),
]