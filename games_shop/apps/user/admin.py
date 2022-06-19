from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email",
                           "password",
                           "gender",
                           "name",
                           "surname",
                           "phone",
                           "birthday",
                           "city",
                           "address",
                           "postal_code",
                           )}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    save_on_top = True
    list_display = ("email", "surname", "name", "is_staff")
    search_fields = ("email", )
    ordering = ("email", "surname", "name")


admin.site.register(User, CustomUserAdmin)
