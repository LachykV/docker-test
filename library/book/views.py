from django.shortcuts import render, get_object_or_404

from .forms import BooksDisplayForm
from .models import Book


def books(request):
    books_all = Book.objects.all()
    form = []
    for the_book in books_all:
        form.append(BooksDisplayForm(instance=the_book))
    return render(request, 'books/books.html', {'form': form})


def book(request, num):
    our_book = get_object_or_404(Book, pk=num)
    form = BooksDisplayForm(instance=our_book)
    return render(request, 'books/book.html', {'form': form})


def index(request):
    return render(request, 'index/index.html')
