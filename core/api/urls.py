from django.urls import path

from core import api
from .views import api_item_list_view


urlpatterns = [
    path("", api_item_list_view, name="api-home")
]