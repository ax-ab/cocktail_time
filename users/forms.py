from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Field

# Allows for custom forms. Remeber to adjust the custom user creation form if different password check is needed etc.
# UserCreationForm has 2 purposes: Allows for user creation in the first place and then also form customization through crispy-forms
class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        #Adding placeholders
        self.helper = FormHelper()
        # Below is to use the bootstrap validation fields instead
        self.helper.attrs = {'novalidate': ''}
        
        self.helper.layout = Layout(
            Field('email',placeholder='Email'),
            Field('password1',placeholder='Password'),
            Field('password2',placeholder='Repeat password'),
            ButtonHolder(
                Submit('register', 'Register', css_class='register-button')
            )
        )
        # Below is to disable the labels for each field
        self.helper.form_show_labels = False

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email',)
        # Add more fields here if needed.

# Only used to modify the form template and no view is implemented as this form is parsed in directly via urls.py
class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        # Below is to use the bootstrap validation fields instead
        self.helper.attrs = {'novalidate': ''}

        self.helper.layout = Layout(
            Field('username',placeholder='Email'),
            Field('password',placeholder='Password'),
            ButtonHolder(
                Submit('login', 'Login', css_class='login-button')
            )
        )
        # Below is to disable the labels for each field
        self.helper.form_show_labels = False

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class UserAdminCreationForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('email',)