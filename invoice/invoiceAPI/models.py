from django.db import models

# Create your models here.
class Invoice(models.Model):
    date = models.DateField()
    customerName = models.CharField(max_length=80)

class InvoiceDetails(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField()