from django.contrib import admin
from .models import Pin

# Register your models here.

@admin.register(Pin)
class PostAdmin(admin.ModelAdmin):
    list_display = ('tittle', 'author')