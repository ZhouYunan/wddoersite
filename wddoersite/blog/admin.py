from django.contrib import admin
from models import Note, Category
from forms import NoteForm



class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_time', )
    list_display_links = ('title', )
    list_filter = ('created_time', 'category', )
    search_fields = ('title', )
    form = NoteForm


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )

admin.site.register(Note, NoteAdmin)
admin.site.register(Category, CategoryAdmin)