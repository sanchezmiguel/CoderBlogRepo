from django import forms
from django.contrib.auth.models import User

from perfilesApp.models import UserProfile


class UserProfileForm(forms.ModelForm):
    avatar = forms.ImageField(required=False, label='Avatar', widget=forms.FileInput)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'avatar']
