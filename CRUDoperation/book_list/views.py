from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .models import BookList
from .forms import BookForm
from django.db.models import Q


class HomeView(View):
    def get(self, request):
        books = BookList.objects.all()
        context = {'books': books}
        return render(request, 'book_list/home.html', context)


class BookAddView(View):
    def get(self, request):
        form = BookForm(label_suffix='')
        context = {'form': form}
        return render(request, 'book_list/book_form.html', context)

    def post(self, request):
        form = BookForm(request.POST, label_suffix='')
        if form.is_valid():
            form.save()
            messages.success(request, f'Book Data Added To The list')
            return redirect('book_list:home')


class BookUpdateView(View):
    def get(self, request, pk):
        book = BookList.objects.get(pk=pk)
        form = BookForm(instance=book, label_suffix='')
        context = {'form': form}
        return render(request, 'book_list/book_form.html', context)

    def post(self, request, pk):
        book = BookList.objects.get(pk=pk)
        form = BookForm(request.POST, instance=book, label_suffix='')
        if form.is_valid():
            form.save()
            messages.success(request, f'Book Data Updated')
            return redirect('book_list:home')


class BookDeleteView(View):
    def get(self, request, pk):
        book = BookList.objects.get(pk=pk)
        context = {'book': book}
        return render(request, 'book_list/book_delete.html', context)

    def post(self, request, pk):
        book = BookList.objects.get(pk=pk)
        book.delete()
        messages.success(request, f'Book Deleted')
        return redirect('book_list:home')


class BookSearchView(View):
    def get(self, request):
        query = request.GET.get('q').strip()
        if query:
            books = BookList.objects.filter(Q(name__icontains=query) | Q(author__icontains=query) |
                                            Q(category__name__icontains=query) | Q(publication__icontains=query))
        else:
            books = BookList.objects.none()
        context = {'books': books, 'query': query}
        return render(request, 'book_list/book_search.html', context)
