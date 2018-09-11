from django.urls import path
from account import views

app_name = 'account'
urlpatterns = [
    path('userCreate/', views.userCreate, name='userCreate'),
    path('userUpdate/<int:pk>/', views.userUpdate, name='userUpdate'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]