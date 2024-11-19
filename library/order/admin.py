from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_number', 'book', 'get_user_full_name', 'get_user_email', 'created_at', 'end_at', 'plated_end_at')
    list_filter = ('book', 'user', 'created_at', 'end_at', 'plated_end_at')

    readonly_fields = ('created_at', 'get_user_full_name', 'get_user_email', 'get_user_role', 'order_number')

    fieldsets = (
        ('Static Information', {
            'fields': ('book', 'order_number', 'get_user_full_name', 'get_user_email', 'get_user_role')
        }),
        ('Dynamic Information', {
            'fields': ('created_at', 'end_at', 'plated_end_at')
        }),
    )

    def order_number(self, obj):
        return obj.id

    order_number.short_description = 'Order Number'

    def get_user_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}" if obj.user.first_name and obj.user.last_name else 'Unknown'

    get_user_full_name.short_description = 'User Full Name'

    def get_user_email(self, obj):
        return obj.user.email if obj.user.email else 'Unknown'

    get_user_email.short_description = 'User Email'

    def get_user_role(self, obj):
        return obj.user.get_role_name() if obj.user.role else 'Unknown'

    get_user_role.short_description = 'User Role'


admin.site.register(Order, OrderAdmin)
