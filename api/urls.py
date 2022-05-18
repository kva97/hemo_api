from django.urls import path, include
from .views import UserRecordView
from rest_framework.authtoken import views as vs
from . import views


app_name = 'api'
urlpatterns = [
    path('', views.getRoutes),
    path('finished_tests/', views.getHemoTests),
    path('create_new_hemotest/', views.createNewHemoTest),
    path('finished_tests/<str:pk>/update_test', views.updateUserData),
    path('finished_tests/<str:pk>/', views.getSpecificHemoTest),
    path('user/', UserRecordView.as_view(), name='users'),
]
