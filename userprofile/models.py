from django.db import models
from register.models import User
from django.utils import timezone
from product.models import Product_Variant

# Create your models here.
class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50,null=False)
    house_name=models.CharField(max_length=100,null=False)
    street_name=models.CharField(max_length=100,null=False)
    pin_number=models.IntegerField(null=False)
    district=models.CharField(max_length=100,null=False)
    state=models.CharField(max_length=50,null=False)
    country=models.CharField(max_length=50,null=False,default="India")
    phone_number=models.CharField(max_length=50,null=False)
    status=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name},{self.house_name},{self.street_name},{self.district},{self.state},{self.country}'
    
    class Meta:
        verbose_name="User Address"
        verbose_name_plural="User Addresses"

class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    variant=models.ForeignKey(Product_Variant,on_delete=models.CASCADE)  
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name}'s wishlist:{self.variant}"
    

class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    updated_at = models.DateField(auto_now_add=True)

    
    def __str__(self):
        return f"{self.user.first_name}'s Wallet"


class WalletTransaction(models.Model):
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=500)
    timestamp = models.DateTimeField(default=timezone.now)
    transaction_type=models.CharField(max_length=500)    

    def __str__(self):
        return f"Transaction of {self.amount} on {self.timestamp}"          