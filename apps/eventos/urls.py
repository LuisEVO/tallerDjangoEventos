from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^categoria/$', CategoriaListView.as_view(), name='categoriaList'),
    url(r'^categoria/crear/$', CategoriaCreateView.as_view(), name='categoriaCreate'),
    url(r'^categoria/actualizar/(?P<pk>\d+)/$', CategoriaUpdateView.as_view(), name='categoriaUpdate'),
    url(r'^categoria/eliminar/(?P<pk>\d+)/$', CategoriaDeleteView.as_view(), name='categoriaDelete'),
    url(r'^categoria/detalle/(?P<pk>\d+)/$', CategoriaDetailView.as_view(), name='categoriaDetail'),

    url(r'^eventos/$', EventoListView.as_view(), name='eventoList'),
    url(r'^eventos/crear/$', EventoCreateView.as_view(), name='eventoCreate'),
    url(r'^eventos/actualizar/(?P<pk>\d+)/$', EventoUpdateView.as_view(), name='eventoUpdate'),
    url(r'^eventos/eliminar/(?P<pk>\d+)/$', EventoDeleteView.as_view(), name='eventoDelete'),
    url(r'^eventos/detalle/(?P<pk>\d+)/$', EventoDetailView.as_view(), name='eventoDetail'),
]