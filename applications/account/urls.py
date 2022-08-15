from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import password_recover, PasswordUserResetTemplateView

urlpatterns = [
    # post views
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('login/', views.user_login, name='login'),

    path('password_reset_url/',
        views.PasswordUserResetTemplateView.as_view(),
        name='password_reset_url'),

    path('password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),

    path('reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
        
    path('register/', views.register, name='register'),
    
    path('accounts/confirm/<activation_key>', views.register_confirm, name='register_confirm'),
        
    #path('password_reset/',
    #    auth_views.PasswordResetView.as_view(),
    #    name='password_reset'),"""
    path('password_reset/',
        views.password_recover,
        name='password_reset'),
]