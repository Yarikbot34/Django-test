from django.urls import path
from . import views, PublicationRedactor

urlpatterns = [
    path('login', views.Userlogin,  name='login'),
    path('register', views.UserRegister,  name='register'),
    path('PassRecovery', views.PassRecov,  name='password_recovery'),
    path('PassRecovery', views.PassRecov,  name='change_password'),
    path('VerifCode', views.RecovCode,  name='verify_code'),
    path('VerifCode/R', views.ResendMail,  name='resend_code'),
    path('profile/', views.Cabinet,  name='cabinet'),
    path('profile/#createstat', PublicationRedactor.NewArt, name = 'create_article'),
    path('profile/delete:<int:id>', PublicationRedactor.DeleteArt, name='article_delete'),
    path('profile/redact:<int:id>', PublicationRedactor.RedactArt, name='article_redact'),
    path('logout', views.UserLogout, name='logout')

]