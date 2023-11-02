from django.contrib import admin

from mensajeriaApp import models

# Register your models here.
admin.site.register(models.Chat)
admin.site.register(models.Message)