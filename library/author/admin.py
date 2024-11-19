from django.contrib import admin

from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronymic', 'id')
    list_filter = ('name', 'books', 'surname', 'id', 'patronymic')
    fieldsets = (
        ('Personal Information', {'fields': (('name', 'patronymic'), 'surname')}),
        ('Related Books', {'fields': ('books',)}),
    )


admin.site.register(Author, AuthorAdmin)
