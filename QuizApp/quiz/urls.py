from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/', views.quiz, name='quiz'),
    path('result/', views.result, name='result'),
    path('add-question/', views.add_question, name='add-question'),
    path('question-list/', views.question_list, name='question-list'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
