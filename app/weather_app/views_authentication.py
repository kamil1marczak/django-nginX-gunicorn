from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.contrib.auth.mixins import UserPassesTestMixin


class SuperUserCheck(UserPassesTestMixin, View):

    def test_func(self):
        return self.request.user.is_superuser


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('books')
        return render(request, 'login.html')

    def post(self, request):
        next_page = request.GET.get('next')
        if next_page is None:
            next_page = 'dashboard'
        user_login = request.POST.get('login')
        user_password = request.POST.get('password')
        user = authenticate(username=user_login, password=user_password)
        if user is not None:
            login(request, user)
            return redirect(next_page)
        else:
            message = 'incorrect login or password'
            return render(request, 'login.html', context={'message': message})



class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')