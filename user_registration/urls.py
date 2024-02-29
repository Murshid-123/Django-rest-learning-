from django.urls import path
from .views import RegistrationView
from rest_framework.authtoken.views import ObtainAuthToken
urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('login', ObtainAuthToken.as_view(), name='login'),
]
