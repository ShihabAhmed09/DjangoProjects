from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="BlogHome"),
    path("blog_post/<int:id>", views.blog_post, name="BlogPost"),
]
