from django.urls import path 
from .views import  home, register
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView) 

urlpatterns = [
    path('home/', home, name="Home"),
    path("token-obtain-pair/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("register/", register, name="Register"),
    path("token-refresh/", TokenRefreshView.as_view(), name="token-refresh"),
]

