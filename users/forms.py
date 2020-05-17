from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Account

class UserCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('username', 'first_name', 'last_name', 'email')

class UserChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = UserChangeForm.Meta.fields