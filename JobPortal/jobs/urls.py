from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apply/<str:company>/<str:position>/', views.apply, name='apply'),
    path('add-job-post/', views.add_job_post, name='add-job-post'),
    path('job-posts/<str:company>/', views.job_posts, name='job-posts'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
