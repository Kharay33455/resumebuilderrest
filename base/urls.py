from django.urls import path
from .views import *

app_name = 'base'

urlpatterns = [
    path("get-user-details", get_user_details, name = "get-user-details")
]