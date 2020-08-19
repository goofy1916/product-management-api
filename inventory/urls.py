from rest_framework.routers import DefaultRouter
from django.urls import path, include
from inventory import views

router = DefaultRouter()
router.register(r'products', views.ProductView, basename='products')
router.register(r'products', views.ProductDetailView, basename='product_details')


urlpatterns = [
    # path('',),
    path('', include(router.urls)),
    # path('products/<int:pk>', include(router.urls)),

]
