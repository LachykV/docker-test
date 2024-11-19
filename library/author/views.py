from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from book.forms import BooksDisplayForm
from .forms import AuthorDisplayForm
from .models import Author


class AuthorListView(ListView):
    model = Author
    template_name = 'author/authors_list_all.html'
    context_object_name = 'authors'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author_forms = []
        for author in context['authors']:
            form = AuthorDisplayForm(instance=author)
            author_forms.append(form)
        context['author_forms'] = author_forms
        return context


class AuthorBooksView(ListView):
    model = Author
    template_name = 'author/author_book_list.html'
    context_object_name = 'book_forms'

    def get_queryset(self):
        author = get_object_or_404(Author, id=self.kwargs['author_id'])
        return author.books_authored.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = get_object_or_404(Author, id=self.kwargs['author_id'])
        context['author'] = author
        book_forms = []
        for book in self.get_queryset():
            form = BooksDisplayForm(instance=book)
            book_forms.append(form)
        context['book_forms'] = book_forms
        return context
