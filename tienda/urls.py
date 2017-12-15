from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'tienda'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index2'),
    url(r'^gugif/$', views.IndexView.as_view(), name='index'),
    url(r'^gugif/f$', views.FacebookView.as_view(), name='facebook'),
    url(r'^gugif/mujer$', views.DamaView.as_view(), name='dama'),
    url(r'^gugif/hombre$', views.HombreView.as_view(), name='hombre'),
    url(r'^gugif/chicos$', views.ChicoView.as_view(), name='chicos'),
    url(r'^gugif/comprar$', views.ComprarView.as_view(), name='comprar'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
