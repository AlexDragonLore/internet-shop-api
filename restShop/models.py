from django.db import models
from django.contrib import admin


class Price(models.Model):
    currency = models.CharField(max_length=20, blank=False)
    value = models.DecimalField(max_digits=5, decimal_places=2, blank=False)

    def __str__(self):
        return str(self.value) + ' ' + str(self.currency)


class Type(models.Model):
    name = models.CharField(max_length=30, blank=False)
    characteristics = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30, blank=False)
    price = models.ForeignKey(Price, on_delete=models.PROTECT, blank=False)
    quantity = models.IntegerField(default=0)
    barcode = models.IntegerField(blank=False)
    dateUpdate = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.name





