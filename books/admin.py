from django.contrib import admin
from .models import Genre, Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year', 'genre')

admin.site.register(Genre)
admin.site.register(Book, BookAdmin)