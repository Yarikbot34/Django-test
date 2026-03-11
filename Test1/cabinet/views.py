import os
import random

from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail


def Userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        # Проверяем пользователя
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Если не "запомнить меня" - сессия закроется при закрытии браузера
            if not remember:
                request.session.set_expiry(0)

            messages.success(request, f'Добро пожаловать, {username}!')
            return redirect('/')  # Перенаправление на главную
        else:
            messages.error(request, 'Неверный логин или пароль')

    return render(request, 'login/login.html')

def UserRegister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if password == request.POST.get('password_confirm') and not(User.objects.filter(username=username).exists()):
            recovcode = random.randint(1000000,9999999)
            send_mail(
                "Код подтверждения",
                f"Здравствуйте {username}, ваш код подтверждения:\n{recovcode}.",
                os.getenv('MAIL_BACK'),
                ['yroslavbot1@gmail.com'],
                fail_silently=False,
            )
            request.session['recovcode'] = recovcode
            request.session['usermail'] = email
            request.session['username'] = username
            request.session['userpass'] = password
            request.session['type'] = 'register'
            return redirect('/VerifCode')
        else:
            messages.error(request, "Не чёт хуйня написана")
            return render(request, 'login/register.html')

    else:
        return render(request, 'login/register.html')

def PassRecov(request):
    if request.method == 'POST':
        pass
    return render(request, 'login/recov.html')

def RecovCode(request):
    if request.session['type'] == 'register' and request.method == 'POST':
        print('register')
        enterrecov = request.POST.get('code')
        print(enterrecov, type(enterrecov))
        print(request.session['recovcode'], type(request.session['recovcode']))
        print(enterrecov == request.session['recovcode'])
        if str(request.session['recovcode']) == enterrecov:
            print('right')
            user = User.objects.create_user(
                username = request.session['username'],
                email = request.session['usermail'],
                password = request.session['userpass']
                )
            del request.session['username'],request.session['userpass'],request.session['usermail'], request.session['type'], request.session['recovcode']
            user.save()
            login(request, user)
            return redirect('/')
        return render(request, 'login/recov_code.html')
    return render(request, 'login/recov_code.html')