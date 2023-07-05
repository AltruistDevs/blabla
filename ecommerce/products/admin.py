from django.contrib import admin
from .models import MenuItem,CartItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'price')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_cart_items')

    def display_cart_items(self, obj):
        return ", ".join(str(item) for item in obj.cart_item.all())

    display_cart_items.short_description = 'Cart Items'