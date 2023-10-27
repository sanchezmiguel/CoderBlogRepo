from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from blogApp.forms import ArticuloForm
from blogApp.models import Articulo


# Create your views here.


class ArticuloListView(ListView):
    model = Articulo
    context_object_name = 'articulos'
