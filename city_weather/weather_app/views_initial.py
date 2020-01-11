from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from weather_app.init_settings import TablePopulator, UserManagement
from weather_app.views_authentication import SuperUserCheck

class InitialData(SuperUserCheck, View):

    def get(self, request):
        return render(request, 'initial/initial_data.html')

    def post(self, request):
        table_creation_checklist = []

        # try:airports_list
        TablePopulator.city_list()
        # table_creation_checklist.append("airport list table created successfully")
        # except:
        #     table_creation_checklist.append("airport list table: error during creation ")



        return render(request, 'initial/initial_data.html', context={'table_creation_checklist': table_creation_checklist

                                                                     })

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