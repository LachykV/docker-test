from django.urls import path
from . import views
from .views import AuthorListView, AuthorBooksView

urlpatterns = [
    path('', AuthorListView.as_view(), name='view_all_authors'),
    path('<int:author_id>/', AuthorBooksView.as_view(), name='author_books'),
]
