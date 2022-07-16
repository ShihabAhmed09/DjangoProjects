from django.urls import path
from .views import HomeView, CandidateView

app_name = 'resume'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('candidate/<str:name>', CandidateView.as_view(), name='candidate-view'),
]
