from django.urls import path
from awbin import views

app_name = 'awbin'
urlpatterns = [
    path('', views.mawbinList, name='mawbinList'),
    path('mawbinList/', views.mawbinList, name='mawbinList'),
    path('mawbinCreate/',views.mawbinCreate, name='mawbinCreate'),
    path('mawbinView/<int:pk>/', views.mawbinView, name='mawbinView'),
    path('mawbinUpdate/<int:pk>/', views.mawbinUpdate, name='mawbinUpdate'),
    path('mawbinDelete/<int:pk>/', views.mawbinDelete, name='mawbinDelete'),
]