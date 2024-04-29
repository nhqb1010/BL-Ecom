from collections.abc import Callable, Sequence
from django.contrib import admin
from django.http import HttpRequest
from typing import Any

from .models import User
from utils.helpers import is_admin_add_url


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ordering = ('-date_joined', )
    search_fields = ["email"]
    list_filter = ("is_staff", "is_active", )
    list_display = ("email", "is_staff", "is_active")


    def get_readonly_fields(self, request, obj=None):
        all_fields = [f.name for f in self.model._meta.fields]

        # Admin cannot update their own account
        if obj is not None and obj.email == request.user.email:
            return all_fields
        
        # Unless 'add' action, only allow admin to update "is_active" field
        return super().get_readonly_fields(request, obj) if is_admin_add_url(request) else [f for f in all_fields if f != "is_active"]
    

    def get_fields(self, request: HttpRequest, obj: Any | None = ...) -> Sequence[Callable[..., Any] | str]:
        return ("email", "password", "is_staff", "is_active") if is_admin_add_url(request) else ("id", "email", "is_superuser", "is_staff", "is_active", "last_login", "date_joined")
    
    
    def has_delete_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return False
    
