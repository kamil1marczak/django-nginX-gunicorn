from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from weather_app.init_settings import TablePopulator, UserManagement
from weather_app.views_authentication import SuperUserCheck


class CreateUser(View):
    @method_decorator(login_required)
    def get(self, request):

        return render(request, 'initial/initial_user.html', context={

        })

    @method_decorator(login_required)
    def post(self, request):
        login = request.POST.get('login')
        email = request.POST.get('email')
        password = request.POST.get('password')

        UserManagement.create_user(login, email, password)
        message = f'user{login} successfully added'


        return render(request, 'initial/initial_user.html', context={
            'message': message
        })