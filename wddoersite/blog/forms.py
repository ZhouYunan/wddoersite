from models import Note
from pagedown.widgets import AdminPagedownWidget
from django import forms



class NoteForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Note
        fields = ('title', 'po_type', 'content')
