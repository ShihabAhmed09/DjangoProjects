from django.urls import path, include
from . import views

app_name = 'main_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('task/<int:pk>/update/', views.update_task, name='update-task'),
    path('task/<int:pk>/delete/', views.delete_task, name='delete-task'),
]
