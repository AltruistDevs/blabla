from django.db import models
from django.contrib.auth.models import User

class MenuItem(models.Model):
    item_name = models.CharField(max_length=20,unique=True)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    
    def __str__(self) -> str:
        return self.item_name
    

class CartItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    cart_item = models.ManyToManyField(MenuItem,related_name='carts')
    
    def __str__(self) -> str:
        return str(self.cart_item)
    
    
    
    
