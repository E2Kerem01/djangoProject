from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Store(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="yazar")
    title = models.CharField(max_length=50, verbose_name="başlık")
    content = models.TextField(verbose_name="içerik")
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


"""class QuickProduct(models.Model):
    name = models.CharField(max_length=100)
    stock_quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50)
    category = models.CharField(max_length=50)  # veya ayrı bir Category modeli olabilir
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2) """

class QuickAdd(models.Model):
    name = models.CharField(max_length=120, unique=True)
    stock = models.PositiveIntegerField()
    maaliyet = models.PositiveIntegerField()
    satisFiyati = models.PositiveIntegerField()
    kdvOrani = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=100)

class QuickProduct(models.Model):
    product_name = models.CharField(max_length=255)
    stock_quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50, blank=True)  # Boş bırakılabilir
    category = models.CharField(max_length=50, blank=True)  # Boş bırakılabilir
    quick_sale = models.CharField(max_length=50, blank=True)  # Boş bırakılabilir
    kdv_rate = models.DecimalField(max_digits=5, decimal_places=2)
    product_image = models.ImageField(upload_to='product_images/', blank=True, null=True)  # Boş bırakılabilir ve null olabilir
