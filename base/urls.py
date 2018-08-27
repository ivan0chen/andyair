from django.urls import path
from main import views as mainViews
from base import views

app_name = 'base'
urlpatterns = [
    path('', mainViews.main, name='base'),
    path('custadvList/', views.custadvList, name='custadvList'),
    path('custadvCreate/', views.custadvCreate, name='custadvCreate'),
    path('custadvView/<int:pk>/', views.custadvView, name='custadvView'),
    path('custadvUpdate/<int:pk>/', views.custadvUpdate, name='custadvUpdate'),
    path('custadvDelete/<int:pk>/', views.custadvDelete, name='custadvDelete'),
    # path('custqtnCreate/<int:parent_pk>/', views.custqtnCreate, name='custqtnCreate'),
    # path('custqtnUpdate/<int:pk>/', views.custqtnUpdate, name='custqtnUpdate'),
    # path('custqtnDelete/<int:pk>/', views.custqtnDelete, name='custqtnDelete'),
    path('custqtnTabledit/', views.custqtnTabledit, name='custqtnTabledit'),
    path('custqtnNew/<int:parent_pk>/', views.custqtnNew, name='custqtnNew'),
]