from django.urls import path, include
from .views import HomeView, BookAddView, BookUpdateView, BookDeleteView, BookSearchView

app_name = 'book_list'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('book/add/', BookAddView.as_view(), name='book-add'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('book/search/', BookSearchView.as_view(), name='book-search'),
]
