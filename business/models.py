from django.db import models
import uuid
from accounts.models import User
# Create your models here.

class Business(models.Model):
    user     = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)
    name     = models.CharField(max_length=100, blank=True,null= True)
    phone    = models.CharField(max_length=100, blank=True,null= True)
    email    = models.EmailField(max_length=100, blank=True,null= True)
    bio      = models.TextField(blank=True,null= True)
    instagram    = models.CharField(max_length=100, blank=True,null= True)
    facebook    = models.CharField(max_length=100, blank=True,null= True)
    twitter    = models.CharField(max_length=100, blank=True,null= True)
    website    = models.CharField(max_length=100, blank=True,null= True)
    postcode = models.CharField(max_length=100, blank=True,null= True)
    address1  = models.CharField(max_length=200, blank=True,null= True)
    address2  = models.CharField(max_length=200, blank=True,null= True)
    town  = models.CharField(max_length=100, blank=True,null= True)
    country     = models.CharField(max_length=100, blank=True, null=True)
    id       = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.name