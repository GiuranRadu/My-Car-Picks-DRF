from django.urls import path
from .views import home, register

# from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from . import views

urlpatterns = [
    path("home/", home, name="Home"),
    path(
        "token-obtain-pair/", views.cookie_token_obtain_pair, name="token-obtain-pair"
    ),
    path("register/", register, name="Register"),
    path("token-refresh/", views.cookie_token_refresh, name="token-refresh"),
    path("protected-route/", views.ProtectedRoute, name="protected-route"),
    path("me/", views.me, name="me"),
]
