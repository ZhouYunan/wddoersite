from models import Note
from wddoersite.pagedown.widgets import AdminPagedownWidget
from django import forms


class NoteForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Note
        fields = ('title', 'is_displayed', 'category', 'content')
