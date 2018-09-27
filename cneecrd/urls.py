from django.urls import path
from cneecrd import views

app_name = 'cneecrd'
urlpatterns = [
    path('cneecrdList/', views.cneecrdList, name='cneecrdList'),
    # path('cneecrdList/', views.CneecrdListView.as_view(), name='cneecrdList'),
    path('cneecrdUpdate/<int:pk>/', views.cneecrdUpdate, name='cneecrdUpdate'),
    # path('cneecrdUpdate/<int:pk>', views.CneecrdUpdateView.as_view(), name='cneecrdUpdate'),
]