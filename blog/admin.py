from django.contrib import admin
from .models import Pin, Comments

# Register your models here.

@admin.register(Pin)
class PostAdmin(admin.ModelAdmin):
    list_display = ('tittle', 'author')

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'text_comment' ,'post')