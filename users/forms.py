from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# Allows for custom forms. Remeber to adjust the custom user creation form if different password check is needed etc.
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email',)
        # Add more fields here if needed.

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class UserAdminCreationForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('email',)