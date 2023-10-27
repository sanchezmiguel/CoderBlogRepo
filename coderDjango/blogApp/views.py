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
    template_name = 'tu_template.html'

    def get_queryset(self):
        # Obtén el valor del parámetro 'orden' de la URL
        orden = self.request.GET.get('orden')

        # Define la consulta base sin ordenamiento
        queryset = Articulo.objects.all()

        # Verifica el valor de 'orden' y ordena los artículos en consecuencia
        if orden == 'title':
            queryset = queryset.order_by('title')
        elif orden == 'author':
            queryset = queryset.order_by('author')
        else:
            queryset = queryset.order_by('created')

        return queryset


class ArticuloDetailView(DetailView):
    model = Articulo
    context_object_name = 'articulo'


class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    success_url = '/pages'
    form_class = ArticuloForm

    def form_valid(self, form):
        form.instance.author = self.request.user  # Asigna el autor al usuario actual
        return super().form_valid(form)


class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    success_url = '/pages'
    form_class = ArticuloForm
