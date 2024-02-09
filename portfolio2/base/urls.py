from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_home, name='base-home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('blog/', views.blog_home, name='blog-home'),
    path('project/<slug:slug>/', views.project_details, name='project-details'),
    path('post/<slug:slug>/', views.post_details, name='post-details'),
]
