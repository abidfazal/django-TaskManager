from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms

INPUT_DES = 'px-5 py-3 rounded-xl border'

class LoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = ('username','password')
        widgets = {
            'usernam':forms.TextInput(attrs={
                'placholder':'enter username',
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'password':forms.PasswordInput(attrs={
                'placeholder':'enter password',
                'class':'px-5 py-3 rounded-xl border'
            }),
        }
        
        
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'enter username',
                'class': 'w-1/2 py-4 px-6 rounded-xl border'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'enter email',
                'class': 'w-1/2 py-4 px-6 rounded-xl border'
            }),
            'password1': forms.PasswordInput(attrs={
                'placeholder': 'enter password',
                'class': 'w-1/2 px-5 py-3 rounded-xl border'
            }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'enter password',
                'class': 'w-1/2 px-5 py-3 rounded-xl border'
            }),
        }
        
        
