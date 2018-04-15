from django.contrib import admin
from .models import Egg

class EggAdmin(admin.ModelAdmin):
    fields = ['egg_code', 'egg_name', 'base_color', 'ornament', 'picture', 'cooked', 'best_before', 'price']
    list_display = ['egg_code', 'egg_name', 'price']
    list_filter = ['egg_code', 'egg_name', 'price']
    search_fields = ['egg_code', 'egg_name', 'base_color', 'cooked', 'best_before', 'price']

# Register your models here.
admin.site.register(Egg, EggAdmin)


