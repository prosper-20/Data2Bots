import imp
from django.urls import path

from core import api
from .views import api_item_list_view, ItemListView, registration_view, account_properties_view, update_user_view
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("", ItemListView.as_view(), name="api-home"),
    path('properties', account_properties_view, name="properties"),
    path("properties/update", update_user_view, name="properties-update"),
    path("register", registration_view, name="register"),
    path("login", obtain_auth_token, name="login"),

]