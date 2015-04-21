from django.contrib import admin
from models import Note, Category



class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'po_type', 'pub_time', )
    list_display_links = ('title', )
    list_filter = ('pub_time', 'po_type', )
    search_fields = ('title', )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )

admin.site.register(Note, NoteAdmin)
admin.site.register(Category, CategoryAdmin)