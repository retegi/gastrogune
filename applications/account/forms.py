from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.ModelForm):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label='Contraseña')

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self,*args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].label = "Usuario / Erabiltzailea"
        self.fields['password'].widget.attrs.update({'class': 'form-control','type':'password'})
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


#clean email field
def clean_email(self):
    email = self.cleaned_data["email"]
    try:
        User._default_manager.get(email=email)
    except User.DoesNotExist:
        return email
    raise forms.ValidationError('email duplicado')

#modificamos el método save() así podemos definir  user.is_active a False la primera vez que se registra
def save(self, commit=True):        
    user = super(RegistrationForm, self).save(commit=False)
    user.email = self.cleaned_data['email']
    if commit:
        user.is_active = False # No está activo hasta que active el vínculo de verificación
        user.save()

    return user


class RegistrationForm(UserCreationForm): #Forma para lo de confirmar por email
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'E-mail address'}))
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def __init__(self,*args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].label = "Nombre de usuario / Erabiltzaile izena"
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].label = "Usuario / Erabiltzailea"
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].label = "Apellido / Abizena"
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].label = "Email / Emaila"
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].label = "Contraseña / Pasahitza"
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].label = "Repetir password / Errepikatu pasahitza"