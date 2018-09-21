from django.urls import path
from shpr import views

app_name = 'shpr'
urlpatterns = [
    path('shprList/', views.shprList, name='shprList'),
    path('shprCreate/',views.shprCreate, name='shprCreate'),
    path('shprView/<int:pk>/', views.shprView, name='shprView'),
    path('shprUpdate/<int:pk>/', views.shprUpdate, name='shprUpdate'),
    path('shprDelete/<int:pk>/', views.shprDelete, name='shprDelete'),
]