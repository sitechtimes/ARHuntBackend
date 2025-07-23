from django.urls import path
from .views import *

urlpatterns = [
    path('rats/', RatView.as_view(), name='rats'),

]