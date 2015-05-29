__author__ = 'wddoer'
# coding:utf-8
from django import forms

from wddoersite.wddoer.models import User


class RegistrationForm(forms.ModelForm):
    """
    Form for registering a new account.
    """
    email = forms.EmailField(widget=forms.TextInput,label="Email")
    password1 = forms.CharField(widget=forms.PasswordInput,
                                label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label="Password (again)")

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def clean_password2(self):
        """
        Check that the two password entries match.
        """
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("二次输入的密码不匹配")
        return password2

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
