from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def account_view(request):
    # Логика для обработки страницы аккаунта
    return render(request, 'accounts/accounts.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:index')
        else:
            # Обработка ошибки аутентификации
            pass
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('main:index')