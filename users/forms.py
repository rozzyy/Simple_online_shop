from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Account
from django import forms 

class UserCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('username', 'first_name', 'last_name', 'email', 'photo', 'address')

class UserChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = UserChangeForm.Meta.fields