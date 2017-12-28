from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'tienda'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^gugif/$', views.BackDoorView.as_view(), name='index2'),
    url(r'^gugif/f$', views.IndexView.as_view(), name='facebook'),
    url(r'^mujer$', views.DamaView.as_view(), name='dama'),
    url(r'^hombre$', views.HombreView.as_view(), name='hombre'),
    url(r'^chicos$', views.ChicoView.as_view(), name='chicos'),
    url(r'^(?P<pk>[0-9]+)$', views.ComprarView.as_view(), name='comprarclick'),
    url(r'^pedido$', views.PedidoView.as_view(), name='pedido'),
    url(r'^opiniones$', views.ComentarioView.as_view(), name='opiniones'),
    url(r'^gracias$', views.GraciasView.as_view(), name='gracias'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
