from django.urls import path
from inpfee import views

app_name = 'inpfee'
urlpatterns = [
    path('inpfeeList/', views.inpfeeList, name='inpfeeList'),
    path('inpfeeCreate/',views.inpfeeCreate, name='inpfeeCreate'),
    path('inpfeeView/<int:pk>/', views.inpfeeView, name='inpfeeView'),
    path('inpfeeUpdate/<int:pk>/', views.inpfeeUpdate, name='inpfeeUpdate'),
    path('inpfeeDelete/<int:pk>/', views.inpfeeDelete, name='inpfeeDelete'),
]