from django.urls import path
from . import views
from .views import (PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView,
                    SearchPostListView)

# app_name = 'blog'
urlpatterns = [
    # path('', views.home, name="blog_home"),
    path('', PostListView.as_view(), name="blog_home"),
    path('search/', SearchPostListView.as_view(), name="search_posts"),
    path('user/<str:username>/', UserPostListView.as_view(), name="user_posts"),
    path('post/new/', PostCreateView.as_view(), name="post_create"),
    # if post_create not work, it's because of post/<slug:slug> or detail view, then just change the name as
    # post/new/create. basically it's try to match 'new' as a slug..
    path('post/<slug:slug>/', PostDetailView.as_view(), name="post_detail"),  # pk is the primary key
    path('post/<slug:slug>/update', PostUpdateView.as_view(), name="post_update"),
    path('post/<slug:slug>/delete', PostDeleteView.as_view(), name="post_delete"),
    path('post_comment', views.post_comment, name='post_comment'),  # API to post a comment
    path('about/', views.about, name="blog_about"),
    path('contact/', views.contact, name="blog_contact"),
]
