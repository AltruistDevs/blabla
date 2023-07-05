from rest_framework import serializers
from .models import MenuItem,CartItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"
        
        
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"