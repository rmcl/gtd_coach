from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth import get_user_model
from authentication.forms import UserChangeForm, UserCreationForm

User = get_user_model()


class UserAdmin(UserAdmin):
    # The forms to add and change user instances
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'email',
                    'password',
                    'password_change_required'
                )
            }
        ),
        ('Personal info', {
            'fields': (
                'first_name',
                'last_name',
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),
        ('Important dates', {
            'fields': (
                'last_login',
            )
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'first_name',
                'last_name',
                'password1',
                'password2'
            )
        }),
    )

    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_staff'
    )

    search_fields = (
        'email',
        'first_name',
        'last_name'
    )
    ordering = (
        'email',
        'last_login',
        'date_joined'
    )


    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            return UserCreationForm
        else:
            return UserChangeForm

admin.site.register(User, UserAdmin)
