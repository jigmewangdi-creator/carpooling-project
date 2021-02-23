from importlib._common import _

from django.forms import ModelForm
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm


class CustomUserCreation(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = "__all__"


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                               label="Username")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               label="Password")

    class Meta:
        model = CustomUser
        fields = ('username', 'password')


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
                   'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
                   }
        error_messages = {
            'username': {
                'max_length': _("The username is too long."),
                'required': True,

            },
        }


# https://blognotes.dev/tutorials/2020/07/21/django-login-with-email-and-username.html
class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
                                   label="Old Password")
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
                                    label="New Password")
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
                                    label="Confirm Password")

    class Meta:
        model = CustomUser
        fields = ('old_password', 'new_password1', 'new_password2')


