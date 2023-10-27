from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


# Create your views here.
class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'perfilesApp/signup.html'
    success_url = '/pages'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('articulo.list')
        return super().get(request, *args, **kwargs)


class LoginInterfaceView(LoginView):
    template_name = 'perfilesApp/login.html'


class LogoutInterfaceView(LogoutView):
    template_name = 'perfilesApp/logout.html'
