from allauth.account.views import confirm_email
from django.contrib import admin
from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    path('users/', UserView.as_view(), name='users'),
    path('rats/', RatView.as_view(), name='rats'),
    path('admin/', admin.site.urls),
    
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('account/', include('allauth.urls')),
    re_path(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
]