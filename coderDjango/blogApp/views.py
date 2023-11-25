from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView
from django.views.generic.edit import DeleteView

from blogApp.forms import ArticuloForm
from .forms import CardSearchForm
from .models import Articulo


# Create your views here.


class ArticuloListView(View):
    model = Articulo
    context_object_name = 'articulos'
    template_name = 'blogApp/articulo_list.html'
    paginate_by = 6  # Set the number of articles per page

    def get(self, request, *args, **kwargs):
        # Obtain the value of the 'orden' parameter from the URL
        orden = self.request.GET.get('orden')

        # Create an instance of the CardSearchForm
        search_form = CardSearchForm(self.request.GET)

        # Check if the form is valid
        if search_form.is_valid():
            search_text = search_form.cleaned_data.get('search_text')
        else:
            search_text = None

        # Define the base queryset without ordering
        queryset = Articulo.objects.all()

        # Filter based on the search_text
        if search_text:
            queryset = queryset.filter(
                Q(title__icontains=search_text) |
                Q(subtitle__icontains=search_text) |
                Q(text__icontains=search_text) |
                Q(author__username__icontains=search_text)
            )

        # Check the value of 'orden' and order the articles accordingly
        if orden == 'title':
            queryset = queryset.order_by('title')
        elif orden == 'author':
            queryset = queryset.order_by('author')
        else:
            queryset = queryset.order_by('created')

        # Paginate the queryset
        page = self.request.GET.get('page', 1)
        paginator = Paginator(queryset, self.paginate_by)

        try:
            articulos = paginator.page(page)
        except PageNotAnInteger:
            articulos = paginator.page(1)
        except EmptyPage:
            articulos = paginator.page(paginator.num_pages)

        context = {'articulos': articulos, 'form': search_form}
        return render(request, self.template_name, context)


class ArticuloDetailView(DetailView):
    model = Articulo
    context_object_name = 'articulo'


class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    success_url = '/pages'
    success_message = "Articulo de blog creado exitosamente!"
    form_class = ArticuloForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    success_url = '/pages'
    success_message = "Articulo de blog actualizado exitosamente!"
    form_class = ArticuloForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Articulo de blog actualizado exitosamente!')
        return super().form_valid(form)


class ArticuloDeleteView(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_message = "Articulo de blog eliminado exitosamente!"
    success_url = '/pages'
    template_name = 'blogApp/articulo_delete.html'
