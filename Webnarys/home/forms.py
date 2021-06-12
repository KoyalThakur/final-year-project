from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import modelformset_factory
from .models import Property


class SignUpForm(UserCreationForm):
   
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address.*')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

PropertyFormset= modelformset_factory(Property, fields=("institute_name", "address", "rent"), extra=1)