from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

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
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
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
    return render(request, 'login/recov_code.html')