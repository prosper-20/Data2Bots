from django.urls import path

from core import api
from .views import api_item_list_view, ItemListView, registration_view


urlpatterns = [
    path("", ItemListView.as_view(), name="api-home"),
    path("register", registration_view, name="register"),

]