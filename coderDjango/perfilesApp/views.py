from django.contrib import messages
# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db import IntegrityError
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

from perfilesApp.models import CreatorProfile
from perfilesApp.models import UserProfile
from .forms import UserProfileForm


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'perfilesApp/signup.html'
    success_url = '/pages'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('articulo.list')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        # Save the user registration data
        response = super().form_valid(form)

        # Create a UserProfile for the new user
        user = self.object  # Get the newly created user
        UserProfile.objects.create(user=user)

        # Log in the user after registration
        login(self.request, user)

        return response


class LoginInterfaceView(LoginView):
    template_name = 'perfilesApp/login.html'


class LogoutInterfaceView(LogoutView):
    template_name = 'perfilesApp/logout.html'


def create_default_creator_profile():
    try:
        CreatorProfile.objects.create(
            name="Pablo Miguel Sanchez Serrano",
            position="Professor and Senior Software Engineer.",
            bio="I am a dedicated and proactive professional known for my unwavering commitment to delivering exceptional results. "
                "With a dynamic and enthusiastic approach to every challenge, "
                "I thrive in collaborative team environments, leveraging strong leadership skills to propel our collective success. "
                "My passion for problem-solving, coupled with analytical prowess, "
                "enables me to break down complex issues and craft innovative solutions that cater to both business objectives and user needs. "
                "I approach each project with boundless enthusiasm and an unyielding commitment to excellence,"
                " consistently striving to surpass expectations."
                "My reputation is built on a track record of delivering high-quality work, consistently on time and within budget. "
                "I take great pride in my ability to not only meet but exceed expectations, "
                "fueling a sense of accomplishment that drives my professional journey",
            email="sanchez.pablo.miguel@gmail.com",
            linkedin="https://www.linkedin.com/in/pablo-miguel-sanchez",
            github="https://github.com/sanchezmiguel"
        )
    except IntegrityError:
        # El perfil ya existe en la base de datos
        pass


def about_creator(request):
    create_default_creator_profile()
    profile = CreatorProfile.objects.first()  # Suponemos que solo tienes un perfil de creador/a
    return render(request, 'perfilesApp/about_creator.html', {'profile': profile})


class ProfileView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'perfilesApp/profile.html'
    success_url = '/pages'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Tu perfil ha sido actualizado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request,
                       'Hubo un error en la actualización de tu perfil. Por favor, verifica los datos ingresados.')
        return super().form_invalid(form)

    def get_object(self, queryset=None):
        return UserProfile.objects.get(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = self.get_object()
        return context
