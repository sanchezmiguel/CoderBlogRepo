from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView
from django.views.generic.edit import DeleteView

from blogApp.forms import ArticuloForm

# Create your views here.

from django.views.generic import ListView
from .models import Articulo
from .forms import CardSearchForm


class ArticuloListView(ListView):
    model = Articulo
    context_object_name = 'articulos'
    template_name = 'blogApp/articulo_list.html'

    def get_queryset(self):
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
            queryset = queryset.filter(text__icontains=search_text)

        # Check the value of 'orden' and order the articles accordingly
        if orden == 'title':
            queryset = queryset.order_by('title')
        elif orden == 'author':
            queryset = queryset.order_by('author')
        else:
            queryset = queryset.order_by('created')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CardSearchForm(self.request.GET)  # Pass the search form to the context
        return context


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


class ArticuloDeleteView(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = '/pages'
    template_name = 'blogApp/articulo_delete.html'
