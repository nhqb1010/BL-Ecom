from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from utils.helpers import is_admin_add_url


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ("-date_joined",)
    search_fields = ["email"]
    list_filter = (
        "is_staff",
        "is_active",
    )
    list_display = ("email", "is_staff", "is_active")

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    fieldsets = (
        (None, {"fields": ("email",)}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    def get_readonly_fields(self, request, obj=None):
        all_fields = [f.name for f in self.model._meta.fields]

        # Admin cannot update their own account
        if obj is not None and obj.email == request.user.email:
            return all_fields

        # Unless 'add' action, only allow admin to update "is_active" field
        return (
            super().get_readonly_fields(request, obj)
            if is_admin_add_url(request)
            else [f for f in all_fields if f != "is_active"]
        )
