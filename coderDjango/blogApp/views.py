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


class ArticuloDetailView(DetailView):
    model = Articulo
    context_object_name = 'articulo'


class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    success_url = '/pages'
    form_class = ArticuloForm
    login_url = '/login'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ArticuloUpdateView(UpdateView):
    model = Articulo
    success_url = '/pages'
    form_class = ArticuloForm