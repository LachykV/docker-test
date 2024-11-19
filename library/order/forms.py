from django import forms
from .models import Order
from book.models import Book
from datetime import timedelta
from django.utils import timezone

class OrderForm(forms.Form):
    book = forms.ModelChoiceField(
        queryset=Book.objects.all(),
        label="Select Book",
        empty_label="Choose a book",
        widget=forms.Select(attrs={'class': 'form-control input'})
    )

    def clean_book(self):
        book = self.cleaned_data.get("book")

        if Order.objects.filter(book=book, end_at=None).exists() and book.count == 1:
            raise forms.ValidationError("This book is already reserved by another user.")

        return book

    def save(self, user):
        plated_end_at = timezone.now() + timedelta(days=14)
        book = self.cleaned_data["book"]
        order = Order.create(user=user, book=book, plated_end_at=plated_end_at)
        return order

