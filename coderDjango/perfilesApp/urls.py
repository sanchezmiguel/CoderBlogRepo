#URLS de PERFILES APP
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # path('', views.HomeView.as_view(),name='home'),
    path('login',views.LoginInterfaceView.as_view(),name='login'),
    path('logout',views.LogoutInterfaceView.as_view(),name='logout'),
    path('signup',views.SignupView.as_view(),name='signup'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)