from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from .models import Product
from .serializers import ProductSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class ProductView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'manufacturer']
    ordering_fields =['name','manufacturer']
    filterset_fields = ['name', 'manufacturer','category']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductDetailView(viewsets.GenericViewSet,mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin ):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)