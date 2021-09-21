from django.db import models
import uuid

# Create your models here.

class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.name

class Service(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)
    name = models.CharField(max_length=200)
    sub_category= models.BooleanField(default=False)
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name