from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.instrumentos, name='instrumentos'),
    url(r'^(?P<instrumento_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add_gaget/$', views.add_gaget, name='add_gaget'),
                       ]

