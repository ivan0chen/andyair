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
    path('hawbinList/<int:parent_pk>/', views.hawbinList, name='hawbinList'),
    path('hawbinCreate/<int:parent_pk>/', views.hawbinCreate, name='hawbinCreate'),
    path('hawbinView/<int:pk>/', views.hawbinView, name='hawbinView'),
    path('hawbinUpdate/<int:pk>/', views.hawbinUpdate, name='hawbinUpdate'),
    path('hawbinDelete/<int:pk>/', views.hawbinDelete, name='hawbinDelete'),
    path('dbnoteNew/<int:parent_pk>/', views.dbnoteNew, name='dbnoteNew'),
    path('debitTabledit/', views.debitTabledit, name='debitTabledit'),
    path('cdnoteNew/<int:parent_pk>/', views.cdnoteNew, name='cdnoteNew'),
    path('creditTabledit/', views.creditTabledit, name='creditTabledit'),
    path('remarkNew/<int:parent_pk>/', views.remarkNew, name='remarkNew'),
    path('remarkTabledit/', views.remarkTabledit, name='remarkTabledit'),
    # path('codNew/<int:parent_pk>/', views.codNew, name='codNew'),
    path('codTabledit/', views.codTabledit, name='codTabledit'),
]