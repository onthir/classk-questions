from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile 
        fields = ('full_name', 'email', 'bio', 'location', )