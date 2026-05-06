from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Rol del usuario', {'fields': ('role',)}),
    )

    list_display = ('username', 'email', 'role', 'is_staff')
    list_filter = ('role', 'is_staff')


admin.site.register(User, CustomUserAdmin)