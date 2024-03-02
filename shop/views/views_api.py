from rest_framework import generics
from shop.models import Item
from shop.serializers import ItemSerializer


class ItemListAPIView(generics.ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class ItemCreateAPIView(generics.CreateAPIView):
    serializer_class = ItemSerializer


class ItemUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class ItemDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class ItemDeleteAPIView(generics.DestroyAPIView):
    queryset = Item.objects.all()
