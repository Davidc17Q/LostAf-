from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
  class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'year')
    search_fields = ('title', 'genre')
    list_filter = ('genre', 'year')