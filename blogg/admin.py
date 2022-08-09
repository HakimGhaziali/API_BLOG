from django.contrib import admin
from .models import GeeksModel


@admin.register(GeeksModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)