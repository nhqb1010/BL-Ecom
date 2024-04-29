from django.contrib import admin
from django.http import HttpRequest
from typing import Any

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ordering = ('-date_joined', )
    fields = ("id", "email", "is_superuser", "is_staff", "is_active", "last_login", "date_joined")
    list_display = ("email", "is_staff", "is_active")
    search_fields = ["email"]
    list_filter = ("is_staff", "is_active", )

    def get_readonly_fields(self, request, obj=None):
        # Make all fields readonly
        return [f.name for f in self.model._meta.fields if f.name != "is_active"]
    
    def has_delete_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return False

