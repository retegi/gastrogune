from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, RegistrationForm
from .models import Profile
from django.core.mail import EmailMultiAlternatives
from django.views.generic import TemplateView

from django.contrib import auth
from django.template import RequestContext
from django.core.mail import send_mail
import datetime
from random import randint
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime, timedelta, timezone, tzinfo
from django.utils.translation import gettext as _

"""def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})"""


"""def register2(request):  #antes se llamaba register
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})"""



#Registro de usuario
def register(request): #Antes se llamaba register_user   
    if request.method == 'POST':
        form = RegistrationForm(request.POST)        
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']           
            activation_key = str(randint(0,10000))
            print(activation_key)         
            key_expires = datetime.now()

            #Obtener el nombre de usuario y guardar estado inactivo
            user=User.objects.get(username=username)
            user.is_active = False
            user.save()

            # Crear el perfil del usuario                                                                                                                                 
            new_profile = Profile(user=user, activation_key=activation_key, key_expires=key_expires)
            new_profile.save()

            # Enviar un email de confirmación
            email_subject = 'Confirmación de registro de usuario / Erabiltzaile berriaren ziurtapena'
            email_body = "Hola %s, Gracias.. Activar: http://127.0.0.1:8000/account/accounts/confirm/%s" % (username, activation_key)

            send_mail(email_subject, email_body, 'info@gastrogune.eus',
                [email], fail_silently=False)
            #return HttpResponseRedirect('registration/email_confirmacion_enviado.html')
            return render(request,'registration/email_confirmacion_enviado.html')
    else:
        form = RegistrationForm()
    return render(request,'registration/register.html',{'user_form': form})



    
def register_confirm(request, activation_key):
    print("Entra en register_confirm")
    # Verifica que el usuario ya está logeado
    """if request.user.is_authenticated():
        HttpResponseRedirect('index')"""

    # Verifica que el token de activación sea válido y sino retorna un 404
    user_profile = get_object_or_404(Profile, activation_key=activation_key)

    # verifica si el token de activación ha expirado y si es así renderiza el html de registro expirado
    """if user_profile.key_expires < datetime.now():
        return render('registration/confirm_expired.html')"""
    # Si el token no ha expirado, se activa el usuario y se muestra el html de confirmación
    user = user_profile.user
    user.is_active = True
    user.save()
    return render(request,'registration/register_confirmado.html')



class PasswordUserResetTemplateView(TemplateView):
    template_name = 'registration/password_reset_form2.html'

    

def password_recover(request): #Antes se llamaba register_user   
    if request.method == 'POST':
        form = RegistrationForm(request.POST)        
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']           
            activation_key = str(randint(0,10000))
            print(activation_key)         
            key_expires = datetime.now()

            #Obtener el nombre de usuario y guardar estado inactivo
            user=User.objects.get(username=username)
            user.is_active = False
            user.save()

            # Crear el perfil del usuario                                                                                                                                 
            new_profile = Profile(user=user, activation_key=activation_key, key_expires=key_expires)
            new_profile.save()

            # Enviar un email de confirmación
            email_subject = 'Confirmación de registro de usuario / Erabiltzaile berriaren ziurtapena'
            email_body = "Hola %s, Gracias.. Activar: http://127.0.0.1:8000/account/accounts/confirm/%s" % (username, activation_key)

            send_mail(email_subject, email_body, 'info@gastrogune.eus',
                [email], fail_silently=False)
            #return HttpResponseRedirect('registration/email_confirmacion_enviado.html')
            return render(request,'registration/email_confirmacion_enviado.html')
    else:
        form = RegistrationForm()
    return render(request,'registration/password_reset_form.html',{'user_form': form})