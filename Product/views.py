from rest_framework import viewsets
from .models import ProductEntry, ProductExit
from .serializers import ProductEntrySerializer, ProductExitSerializer


class ProductEntryView(viewsets.ModelViewSet):
    queryset = ProductEntry.objects.all()
    serializer_class = ProductEntrySerializer
    http_method_names = ['get', 'post', 'put']


class ProductExitView(viewsets.ModelViewSet):
    queryset = ProductExit.objects.all()
    serializer_class = ProductExitSerializer
    http_method_names = ['get', 'post', 'put']