from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_provider = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_staff    = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=False)
    policy_agreed = models.BooleanField()
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login  = models.DateTimeField(auto_now_add=True)
    full_name   = models.CharField(max_length=100, blank=True,null= True)
    username    = models.CharField(max_length=100, blank=True,null= True, unique=True)
    email       = models.EmailField(max_length=100,unique=True)
    mobile      = models.CharField(max_length=100, blank=True,null= True)
    photo       = models.ImageField(null=True,blank=True, default="stanar-display-placeholder.jpg")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= [
        'username','full_name','policy_agreed'
    ]

class Customer(models.Model):
    user     = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)
    id       = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True, editable=False)
