from django import forms

from .models import Book


class BooksDisplayForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'count', 'authors']
        widgets = {
            'name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'description': forms.Textarea(attrs={'readonly': 'readonly'}),
            'count': forms.NumberInput(attrs={'readonly': 'readonly'}),
            'authors': forms.SelectMultiple(attrs={'readonly': 'readonly'})
        }