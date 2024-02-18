from django.contrib import admin
from django.urls import path
from .views import createInvoice, createInvoiceDetails, updateInvoiceDetails

urlpatterns = [
    path('createInvoice/', createInvoice),
    path('createInvoiceDetails/', createInvoiceDetails),
    path('updateInvoiceDetails/', updateInvoiceDetails)
]
