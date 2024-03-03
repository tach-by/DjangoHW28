from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm
)

from django import forms
from django.forms.widgets import (
    TextInput,
    PasswordInput
)

from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())