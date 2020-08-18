from rest_framework.routers import DefaultRouter
from django.urls import path, include
from inventory import views

router = DefaultRouter()
router.register(r'products', views.ProductView, basename='products')

urlpatterns = [
    # path('',),
    path('', include(router.urls)),
]
