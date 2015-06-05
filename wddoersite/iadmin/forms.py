# coding:utf-8
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from wddoersite.blog.models import Note, Category
from django import forms
from models import User
from django.utils.translation import ugettext_lazy as _


class CategoryCreateForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'is_displayed']


class NoteCreateForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ['title', 'is_displayed', 'category', 'content']


class UserCreateForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    email = forms.EmailField(label=_("Email"), widget=forms.TextInput,
                             help_text=_("Enter a valid email address"))
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput,
                                help_text=_("Enter the same password as above, for verification"))

    class Meta:
        model = User
        fields = ("email", )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
