from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'count')
    list_filter = ('authors', 'name', 'id')

    fieldsets = (
        ('Book info', {
            'fields': ('name', 'description')
        }),
        ('Availability', {
            'fields': ('count',)
        }),
        ('Authors', {
            'fields': ('authors',)
        }),
    )


admin.site.register(Book, BookAdmin)
