from rest_framework import status
from rest_framework.response  import Response
from .serializers import ItemSerializer
from rest_framework.decorators import api_view
from core.models import Item
from rest_framework.generics import ListCreateAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated


@api_view(["GET"])
def api_item_list_view(request):
    try:
        items = Item.objects.all()
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)



class ItemListView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
