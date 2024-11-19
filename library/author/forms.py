from django import forms

from .models import Author


class AuthorDisplayForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic']
        widgets = {
            'name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'surname': forms.TextInput(attrs={'readonly': 'readonly'}),
            'patronymic': forms.TextInput(attrs={'readonly': 'readonly'})
        }