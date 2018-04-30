"""cmpe172 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views as root_views
from . import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('searchresults/', TemplateView.as_view(template_name='searchresults.html'), name='searchresults'),
    path('searchresults2/', TemplateView.as_view(template_name='searchresults2.html'), name='searchresults2'),
    path('deptsearch/', TemplateView.as_view(template_name='deptsearch.html'), name='deptsearch'),
]
