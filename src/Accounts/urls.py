from django.urls import path
from Accounts import views

urlpatterns = [
    path('api/register/', views.RegisterAPI, name = "RegisterAPI")
]
