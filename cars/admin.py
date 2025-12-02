from django.contrib import admin
from .models import Car

# Register your models here.


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Car._meta.get_fields()]
    # list_display = ("id", "brand", "model")
    list_filter = ('brand',)
    search_fields = ('brand', 'model')
    autocomplete_fields = ('creator',)
    
