from django.shortcuts import render
from rest_framework.generics import ListAPIView

from inventory.models import Inventory
from inventory.serializers import InventorySerializer


# Create your views here.
class InventoryListView(ListAPIView):
    """
        API to provide list of all inventories
    """
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer