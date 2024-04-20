from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Author, Story


class AuthorAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'name', 'email'),
        }),
    )
    list_display = ('username', 'name', 'email', 'is_staff')
    search_fields = ('username', 'name', 'email')
    ordering = ('username',)


admin.site.register(Author, AuthorAdmin)

admin.site.register(Story)
