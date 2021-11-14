from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, ugettext_lazy as _
from django.core import validators
from . models import Post

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Password'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']
        labels = {'email':'Email Address','first_name':'Address'}

        widgets = {'username':forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Username'}),
        'email':forms.EmailInput(attrs={'class':'form-control my-2', 'placeholder':'Email Address'}),
        'first_name':forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Address'}),
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control my-2', 'placeholder':'Username'}))
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control my-2', 'placeholder':'Password'}))



class DetailsRegistration(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'email', 'password', 'address']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
        }