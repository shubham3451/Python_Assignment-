from django.contrib import admin
from .models import UserData

@admin.register(UserData)
class UserSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    search_fields = ('name', 'email')
    ordering = ('-submitted_at',)

