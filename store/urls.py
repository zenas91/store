from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from . import views


router = DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet, basename='carts')
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet, basename='orders')

product_router = NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', views.ReviewViewSet,
                        basename='product-reviews')
product_router.register('images', views.ProductImageViewSet,
                        basename='product-images')

cart_router = NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', views.CartItemViewSet, basename='cart-items')

order_router = NestedDefaultRouter(router, 'orders', lookup='order')
order_router.register('items', views.OrderItemViewSet, basename='order-items')
# URLConf
urlpatterns = router.urls + product_router.urls + \
    cart_router.urls + order_router.urls
