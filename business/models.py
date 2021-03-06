from django.db import models
import uuid
from accounts.models import User
from services.models import Service as StanarServices
# Create your models here.

class Business(models.Model):
    user     = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)
    business_name     = models.CharField(max_length=100)
    business_phone    = models.CharField(max_length=100)
    business_email    = models.EmailField(max_length=100)
    business_bio      = models.TextField(blank=True)
    instagram_link    = models.CharField(max_length=100, blank=True,null= True)
    facebook_link     = models.CharField(max_length=100, blank=True,null= True)
    twitter_link      = models.CharField(max_length=100, blank=True,null= True)
    website           = models.CharField(max_length=100, blank=True,null= True)
    postcode = models.CharField(max_length=100)
    address_line_1  = models.CharField(max_length=200)
    address_line_2  = models.CharField(max_length=200, blank=True,null= True)
    town  = models.CharField(max_length=100)
    country     = models.CharField(max_length=100)
    id       = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.business_name

class Amenities(models.Model):
    business        = models.OneToOneField(Business, on_delete=models.CASCADE, null=True,blank=True)
    cus_parking     = models.CharField(max_length=10,default='off',blank=True,null= True)
    card_accept     = models.CharField(max_length=10,default='off',blank=True,null= True)
    disability      = models.CharField(max_length=10,default='off',blank=True,null= True)
    child_friendly  = models.CharField(max_length=10,default='off',blank=True,null= True)
    pet_friendly    = models.CharField(max_length=10,default='off',blank=True,null= True)
    wifi            = models.CharField(max_length=10,default='off',blank=True,null= True)
    loyalty_program = models.CharField(max_length=10,default='off',blank=True,null= True)
    
    def __str__(self) -> str:
        return self.business

class PaymentMethods(models.Model):
    business        = models.OneToOneField(Business, on_delete=models.CASCADE, null=True,blank=True)
    cash            = models.CharField(max_length=10,default='off',blank=True,null= True)
    physical        = models.CharField(max_length=10,default='off',blank=True,null= True)
    check           = models.CharField(max_length=10,default='off',blank=True,null= True)
    paypal          = models.CharField(max_length=10,default='off',blank=True,null= True)
    bank_transfer   = models.CharField(max_length=10,default='off',blank=True,null= True)
    gift_card       = models.CharField(max_length=10,default='off',blank=True,null= True)
    
    def __str__(self) -> str:
        return self.business

class Photos(models.Model):
    business        = models.OneToOneField(Business, on_delete=models.CASCADE, null=True,blank=True)
    logo            = models.ImageField(null=True,blank=True, default="stanar-logo-placeholder.jpg")
    banner          = models.ImageField(null=True,blank=True, default="stanar-banner-placeholder.jpg")
    display_1       = models.ImageField(null=True,blank=True, default="stanar-display-placeholder.jpg")
    display_2       = models.ImageField(null=True,blank=True, default="stanar-display-placeholder.jpg")
    display_3       = models.ImageField(null=True,blank=True, default="stanar-display-placeholder.jpg")
    display_4       = models.ImageField(null=True,blank=True, default="stanar-display-placeholder.jpg")
    
    def __str__(self) -> str:
        return self.business

class Service(models.Model):
    business = models.ForeignKey(Business,null=True,blank=True,on_delete=models.CASCADE)
    duration_hours = models.CharField(max_length=2,blank=True,null=True,default='00')
    duration_mins  = models.CharField(max_length=2,blank=True,null=True,default='00')
    price   = models.FloatField(default=0.00)
    note    = models.TextField(max_length=300, blank=True,null=True)
    service =models.ForeignKey(StanarServices,on_delete=models.CASCADE,null=True)

    def __str__(self) -> str:
        return self.business

class Staff(models.Model):
    business =models.ForeignKey(Business,on_delete=models.CASCADE, null=True,blank=True)
    user    = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)
    id       = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True, editable=False)

class StaffService(models.Model):
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE, null=True,blank=True)
    service  = models.ForeignKey(Service, on_delete=models.CASCADE, null=True,blank=True)
    is_active = models.BooleanField(default=True)