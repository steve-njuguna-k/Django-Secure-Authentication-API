from django.urls import path
from Accounts import views

urlpatterns = [
    path('api/register/', views.RegisterAPI, name = "RegisterAPI"),
    path('api/login/', views.LoginAPI, name = "LoginAPI"),
    path('api/user/', views.UserAPI, name = "UserAPI"),
    path('api/logout/', views.LogoutAPI, name = "LogoutAPI"),
]
