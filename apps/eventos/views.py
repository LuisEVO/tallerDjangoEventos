from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic import TemplateView

from .models import *
from .forms import *


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria/listar.html'


class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = 'categoria/formulario.html'
    fields = ('__all__')
    success_url = reverse_lazy('eventos:categoriaList')


class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = 'categoria/formulario.html'
    fields = ('__all__')
    success_url = reverse_lazy('eventos:categoriaList')


class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categoria/eliminar.html'
    success_url = reverse_lazy('eventos:categoriaList')


class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'categoria/detalle.html'


class EventoListView(ListView):
    model = Evento
    template_name = 'eventos/listar.html'

    def get_queryset(self):
        queryset = super(EventoListView, self).get_queryset()
        queryset = queryset.filter(organizador=self.request.user)

        return queryset


class EventoCreateView(CreateView):
    model = Evento
    template_name = 'eventos/formulario.html'
    form_class = EventoForm
    success_url = reverse_lazy('eventos:eventoList')

    def get_initial(self):
        return {
            'organizador':self.request.user
        }


class EventoUpdateView(UpdateView):
    model = Evento
    template_name = 'eventos/formulario.html'
    form_class = EventoForm
    success_url = reverse_lazy('eventos:eventoList')


class EventoDeleteView(DeleteView):
    model = Evento
    template_name = 'eventos/eliminar.html'
    success_url = reverse_lazy('eventos:eventoList')


class EventoDetailView(DetailView):
    model = Evento
    template_name = 'eventos/detalle.html'


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['eventos'] = Evento.objects.all()
        context['categorias'] = Categoria.objects.all()
        context['organizadores'] = User.objects.all()

        return context

