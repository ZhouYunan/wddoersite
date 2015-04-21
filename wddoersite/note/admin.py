from django.contrib import admin
from models import Note, Category



class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pub_time', 'po_type', )
    list_display_links = ('title', )
    list_filter = ('pub_time', 'po_type', )
    search_fields = ('title', 'po_type', )


admin.site.register(Note, NoteAdmin)
admin.site.register(Category)