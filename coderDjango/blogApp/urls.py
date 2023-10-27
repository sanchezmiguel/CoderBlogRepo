#URLS BLOG APP

from django.urls import path
from . import views
urlpatterns=[
    path('',views.ArticuloListView.as_view(),name='articulo.list'),
    path('<int:pk>',views.ArticuloDetailView.as_view(),name='articulo.detail'),
    path('<int:pk>/edit',views.ArticuloUpdateView.as_view(),name='articulo.update'),
    # path('<int:pk>/delete',views.ArticuloDeleteView.as_view(),name='articulo.delete'),
    path('new',views.ArticuloCreateView.as_view(),name='articulo.new'),
]
