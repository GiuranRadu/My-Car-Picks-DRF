from django.contrib import admin
from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'year', 'user', 'created_at')
    list_filter = ('brand', 'year', 'created_at')
    search_fields = ('brand', 'model', 'user__email')
