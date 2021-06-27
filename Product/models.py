from django.db import models
from django.utils import timezone
from .config import *
from django.core.validators import MinValueValidator

from datetime import datetime, timedelta


# Create your models here.
class ProductEntry(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default=OTHERS)
    cost_price = models.FloatField(null=False)
    expiry_date = models.DateField(default=(datetime.now() + timedelta(days=10000)).date())
    count = models.IntegerField(null=False, default=1, validators=[MinValueValidator(0)])
    specs = models.CharField(max_length=50, null=False)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)
    is_sold = models.BooleanField(default=False)
    brand = models.CharField(max_length=30, null=True)

    def __str__(self):
        if self.brand is not None:
            return f'{self.brand} {self.name} - {self.specs}'
        else:
            return f'{self.name} - {self.specs}'

    def save(self, *args, **kwargs):
        self.is_sold = True if self.count <= 0 else False
        data = ProductExit.objects.filter(product_entry=self.id)
        for record in data:
            selling_price = ProductExit.objects.get(id=record.id).selling_price
            ProductExit.objects.filter(id=record.id).update(profit=selling_price-self.cost_price)
        return super(ProductEntry, self).save(*args, **kwargs)


class ProductExit(models.Model):
    product_entry = models.ForeignKey(ProductEntry, to_field='id', on_delete=models.CASCADE)
    selling_price = models.FloatField(null=False)
    profit = models.FloatField(null=True, blank=True)
    count = models.IntegerField(null=False, validators=[MinValueValidator(0)])
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        product_entry_count = ProductEntry.objects.get(id=self.product_entry.id).count
        ProductEntry.objects.filter(id=self.product_entry.id).update(is_sold=True if product_entry_count <= 0 else False)
        self.profit = self.selling_price - ProductEntry.objects.get(id=self.product_entry.id).cost_price
        return super(ProductExit, self).save(*args, **kwargs)
