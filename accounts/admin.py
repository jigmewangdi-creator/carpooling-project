from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreation
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreation

    fieldsets = (
        *UserAdmin.fieldsets, (
            'Permissions', {
                'fields': (
                    'is_vehicle_owner',
                )
            }
        )

    )


admin.site.register(CustomUser, CustomUserAdmin)
