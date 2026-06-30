from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "register_number",
        "full_name",
        "department",
        "semester",
        "email",
    )

    search_fields = (
        "full_name",
        "register_number",
        "email",
    )

    list_filter = (
        "department",
        "semester",
    )

    ordering = ("register_number",)