from rest_framework import serializers
from core.models import Item


class ItemSerializer(serializers.ModelSerializer):
    model = Item

    fields = ["title", "price", "slug"]
