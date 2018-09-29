"""andyair URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include, re_path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls', namespace='main')),
    path('account/', include('account.urls',namespace='account')),
    path('custadv/', include('custadv.urls', namespace='custadv')),
    path('custcsn/', include('custcsn.urls', namespace='custcsn')),
    path('shpr/', include('shpr.urls', namespace='shpr')),
    path('inprmk/', include('inprmk.urls', namespace='inprmk')),
    path('inpfee/', include('inpfee.urls', namespace='inpfee')),
    path('cneecrd/', include('cneecrd.urls', namespace='cneecrd')),
    path('invpars/', include('invpars.urls', namespace='invpars')),
    path('exrate/', include('exrate.urls', namespace='exrate')),
    re_path('.*', views.main),
]
