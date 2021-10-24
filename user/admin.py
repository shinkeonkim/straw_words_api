"Module for Admin View of user app"

from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin View for User."""

    list_display = ("id", "email", "nickname")
    search_fields = ("nickname", "id")
    ordering = ("id", "updated_at")
