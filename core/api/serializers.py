from rest_framework import serializers
from core.models import Item


class ItemSerializers(serializers.ModelSerializer):
    model = Item

    fields = ["title", "price", "slug"]
