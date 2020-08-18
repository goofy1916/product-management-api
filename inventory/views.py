from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from .models import Product
from .serializers import ProductSerializer
# Create your views here.


class ProductView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)