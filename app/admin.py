from django.contrib import admin
from .models import Word

class WordAdmin(admin.ModelAdmin):
    list_display = ('russian', 'english', 'time_create', 'time_update')
    search_fields = ('russian', 'english')


admin.site.register(Word, WordAdmin)