# authentication/admin.py
from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'role', 'is_active', 'is_staff', 'is_superuser', 'created_at', 'updated_at')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'role')


admin.site.register(CustomUser, CustomUserAdmin)
