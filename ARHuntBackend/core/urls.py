from allauth.account.views import confirm_email
from django.contrib import admin
from django.urls import path, include,re_path
from .views import *

urlpatterns = [
    path('rats/', RatView.as_view(), name='rats'),
    path('create_rats/', InitRats.as_view(), name='create_rats'),
    path('admin/', admin.site.urls),
    re_path(r'^rest-auth/', include('dj_rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    re_path(r'^account/', include('allauth.urls')),
    re_path(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
]