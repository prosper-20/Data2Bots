from django.urls import path

from core import api
from .views import api_item_list_view, ItemListView, 


urlpatterns = [
    path("", ItemListView, name="api-home"),
    path("register", registration_view, name="register"),

]