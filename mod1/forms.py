from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(
            attrs={
                'style': 'border-color: blue;',
                'placeholder': 'Write your name here'
            }))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    address=forms.CharField(max_length=500,required=False,help_text='enter address')
    oraganization=forms.CharField(max_length=50,required=True,help_text='please enter the company')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','address','oraganization' )

class userloginform(forms.Form):
	username=forms.CharField(widget=forms.TextInput(
            attrs={
                'style': 'border-color: blue;float:centre;'
            }),label='username')
	password=forms.CharField(label=' password',widget=forms.PasswordInput(attrs={'style': 'float:centre'}))

	class Meta:
		model=User
		fields=('username','password')