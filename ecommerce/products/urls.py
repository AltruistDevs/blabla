from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewset,CartItemViewset



router = DefaultRouter()
router.register(r'products',MenuItemViewset)
router.register(r'cart',CartItemViewset)

urlpatterns = [
    path('',include(router.urls))
]

