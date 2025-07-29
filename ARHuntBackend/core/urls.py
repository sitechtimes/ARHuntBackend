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
    path('users/<str:name>', UserByName.as_view(), name='user_by_name'),
    path('rats/', RatView.as_view(), name='rats'),
    path('catch_rat',CatchRat.as_view(),name='catch_rat'),
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),


]