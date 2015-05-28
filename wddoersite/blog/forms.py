from models import Note, Category
from wddoersite.pagedown.widgets import AdminPagedownWidget
from django import forms


class NoteForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Note
        fields = ('title', 'is_displayed', 'category', 'content')


class CategoryCreateForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name', 'is_displayed')