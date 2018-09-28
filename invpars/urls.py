from django.urls import path
from invpars import views

app_name = 'invpars'
urlpatterns = [
    path('invparsList/', views.invparsList, name='invparsList'),
    path('invparsUpdate/<int:pk>/', views.invparsUpdate, name='invparsUpdate'),
    path('invstkTabledit/', views.invstkTabledit, name='invstkTabledit'),
    path('invstkNew/<int:parent_pk>/', views.invstkNew, name='invstkNew'),
]