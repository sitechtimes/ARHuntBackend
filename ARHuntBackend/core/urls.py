from django.urls import path
from .views import *

urlpatterns = [
    path('rats/', RatView.as_view(), name='rats'),
    path('create_rats/', InitRats.as_view(), name='create_rats'),
]