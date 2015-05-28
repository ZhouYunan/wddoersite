from wddoersite.blog.models import Note, Category
from django import forms


class CategoryCreateForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name', 'is_displayed')