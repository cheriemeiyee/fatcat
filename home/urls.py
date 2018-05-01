from django.conf.urls import url, include
from . import views


urlpatterns = [
    url('^$', views.index),
    url(r'^dashboard', views.dashboard),
    url(r'^', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^', include('social_django.urls', namespace='social')),
    url(r'^deptsearch', views.deptsearch),
    url(r'^results', views.search, name="search"),
    url(r'^addemployee', views.addemployee, name="addemployee"),
    url(r'^employee', views.employee, name='employee'),
    url(r'^allresults', views.allresults, name='allresults'),
]