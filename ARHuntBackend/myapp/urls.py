from django.urls import path
from .views import *

urlpatterns = [
    path('rats/', RatsView.as_view(), name='quiz_list'),

]