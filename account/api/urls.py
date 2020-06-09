from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = 'account'

urlpatterns = [
    path('accounts/', views.getAllUsers),
    path('accounts/signup', views.signUp),
    path('accounts/signin', obtain_auth_token),
    path('accounts/signout', views.Logout),
    path('accounts/current', views.getCurrentUser),
    path('accounts/<int:pk>', views.getUser),
]
