from configparser import MAX_INTERPOLATION_DEPTH
from django.db import models


class Product(models.Model):
    medicine_id = models.AutoField(primary_key=True)
    sku = models.IntegerField(unique=True, null=False)
    medicine = models.CharField(
        max_length=100, null=False, verbose_name="Product")
    description = models.TextField(
        max_length=200, verbose_name='Description', null=False)
    active = models.BooleanField()
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.medicine


class Stock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    medicine = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_ingress = models.DateField()
    date_expiration = models.DateField()

    def __str__(self):
        row = self.medicine.medicine + ' -Stock:  ' + str(self.quantity)
        return row


class Price(models.Model):
    price_id = models.AutoField(primary_key=True)
    medicine = models.ForeignKey(Product, on_delete=models.CASCADE)
    price_buy = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=False)
    price_sell = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=False)

    def __str__(self):
        row = self.medicine.medicine + " - $" + str(self.price_sell)
        return row


class Provider(models.Model):
    provider_id = models.AutoField(primary_key=True)
    provider_name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.provider_name + " - Provider_id: " + str(self.provider_id)


class Provider_medicine(models.Model):
    medicine_provider_id = models.AutoField(primary_key=True)
    medicine = models.ForeignKey(Product, on_delete=models.CASCADE)
    provider = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.medicine.medicine} - Provider_id: {self.provider}"
