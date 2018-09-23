from django.urls import path
from inprmk import views

app_name = 'inprmk'
urlpatterns = [
    path('inprmkList/', views.inprmkList, name='inprmkList'),
    path('inprmkCreate/',views.inprmkCreate, name='inprmkCreate'),
    path('inprmkView/<int:pk>/', views.inprmkView, name='inprmkView'),
    path('inprmkUpdate/<int:pk>/', views.inprmkUpdate, name='inprmkUpdate'),
    path('inprmkDelete/<int:pk>/', views.inprmkDelete, name='inprmkDelete'),
]