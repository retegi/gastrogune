from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self,*args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].label = "Nombre de usuario / Erabiltzailea"
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].label = "Contraseña / Pasahitza"




class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
    
    def __init__(self,*args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].label = "Usuario / Erabiltzailea"
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].label = "Apellido / Abizena"
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].label = "Email / Emaila"
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].label = "Contraseña / Pasahitza"
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].label = "Repetir password / Errepikatu pasahitza"

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']