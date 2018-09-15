from django.urls import path
from main import views as mainViews
from custadv import views

app_name = 'custadv'
urlpatterns = [
    path('', mainViews.main, name='custadv'),
    path('custadvList/', views.custadvList, name='custadvList'),
    path('custadvCreate/', views.custadvCreate, name='custadvCreate'),
    path('custadvView/<int:pk>/', views.custadvView, name='custadvView'),
    path('custadvUpdate/<int:pk>/', views.custadvUpdate, name='custadvUpdate'),
    path('custadvDelete/<int:pk>/', views.custadvDelete, name='custadvDelete'),
    path('custqtnTabledit/', views.custqtnTabledit, name='custqtnTabledit'),
    path('custqtnNew/<int:parent_pk>/', views.custqtnNew, name='custqtnNew'),
    path('custadvData/<int:pk>/', views.custadvData, name='custadvData'),
]