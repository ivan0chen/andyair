from django.urls import path
from exrate import views

app_name = 'exrate'
urlpatterns = [
    path('exrateList/', views.exrateList, name='exrateList'),
    path('exrateCreate/',views.exrateCreate, name='exrateCreate'),
    path('exrateUpdate/<int:pk>/', views.exrateUpdate, name='exrateUpdate'),
    path('exrateDelete/<int:pk>/', views.exrateDelete, name='exrateDelete'),
]