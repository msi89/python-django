from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
# from rest_framework.routers import SimpleRouter

# router = SimpleRouter()
# router.register(r'accounts', AccountViewSet)

app_name = 'account'

urlpatterns = [
    path('accounts/', views.getAllUsers),
    path('accounts/signup', views.signUp),
    path('accounts/signin', obtain_auth_token),
    path('accounts/current', views.getCurrentUser),
    path('accounts/<int:pk>', views.getUser),
    # * router.urls
]
