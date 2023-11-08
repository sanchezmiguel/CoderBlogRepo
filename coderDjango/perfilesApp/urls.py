# URLS de PERFILES APP
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView

from . import views

urlpatterns = [
    # path('', views.HomeView.as_view(),name='home'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup', views.SignupView.as_view(), name='signup'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('cambiar-contrasena/', login_required(PasswordChangeView.as_view()), name='cambiar-contrasena'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
