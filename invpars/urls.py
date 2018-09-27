from django.urls import path
from invpars import views

app_name = 'invpars'
urlpatterns = [
    path('invparsEdit/', views.invparsEdit, name='invparsEdit'),
    path('invstkTabledit/', views.invstkTabledit, name='invstkTabledit'),
    path('invstkNew/<int:parent_pk>/', views.invstkNew, name='invstkNew'),
]