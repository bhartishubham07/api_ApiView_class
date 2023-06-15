from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    PC_id = models.IntegerField()
    PC_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.PC_name
    
    
class Product(models.Model):
    PC_name = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    P_id = models.IntegerField()
    P_name = models.CharField(max_length=100)
    P_price = models.DecimalField(max_digits=10, decimal_places=2)
    P_description = models.TextField()
    P_date = models.DateField()
    
    def __str__(self):
        return self.P_name