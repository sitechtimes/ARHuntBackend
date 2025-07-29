from allauth.account.views import confirm_email
from django.contrib import admin
from django.urls import path, re_path, include
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
urlpatterns = [
    path('users/', UserView.as_view(), name='users'),
    path('rats/', RatView.as_view(), name='rats'),
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('files/', ListFoldersView.as_view(), name='list-folders'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),


]