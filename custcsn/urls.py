from django.urls import path
from custcsn import views

app_name = 'custcsn'
urlpatterns = [
    path('custcsnList/', views.custcsnList, name='custcsnList'),
    path('custcsnCreate/',views.custcnsCreate, name='custcsnCreate'),
    path('custcsnView/<int:pk>/', views.custcsnView, name='custcsnView'),
    path('custcsnUpdate/<int:pk>/', views.custcsnUpdate, name='custcsnUpdate'),
    path('custcsnDelete/<int:pk>/', views.custcsnDelete, name='custcsnDelete'),
]