from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views  # Ensure this line is present

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home view
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Login view
    path('tasks/', include('to_do_list.urls', namespace='to_do_list')),  # To-Do List URLs
    path('blog/', include('blog.urls')),  # Blog URLs
    path('upload_notes/', include('upload_notes.urls')),  # Upload Notes URLs
]
