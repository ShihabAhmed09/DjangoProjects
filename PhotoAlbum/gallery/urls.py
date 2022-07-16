from django.urls import path
from . import views

app_name = 'gallery'
urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('add/', views.add_photo, name='add-photo'),
    path('photo/<str:pk>/', views.photo_view, name='photo-view'),
]
