from rest_framework.viewsets import ModelViewSet
from .serializers import MenuItemSerializer,CartSerializer
from .models import MenuItem,CartItem
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status



class MenuItemViewset(ModelViewSet):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()
    
class CartItemViewset(ModelViewSet):
    serializer_class  = CartSerializer
    queryset = CartItem.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = "id"
    
    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def destroy(self, request, *args, **kwargs):
        cart_item = self.get_object()
        if cart_item.cart_item.exists():
            cart_item.cart_item.clear()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)