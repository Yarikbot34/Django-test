from django.urls import path
from . import views

urlpatterns = [
    path('login', views.Userlogin,  name='login'),
    path('register', views.UserRegister,  name='register'),
    path('PassRecovery', views.PassRecov,  name='password_recovery'),
    path('VerifCode', views.RecovCode,  name='verify_code'),
    path('VerifCode/R', views.ResendMail,  name='resend_code')
]