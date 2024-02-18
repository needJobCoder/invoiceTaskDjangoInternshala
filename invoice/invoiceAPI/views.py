from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Invoice, InvoiceDetails
import datetime

# Create your views here.
@api_view(['POST'])
def createInvoice(request):
    invoice_date = request.data
    
    try:
        customerName = invoice_date['customerName']
    except KeyError:
        return Response({"createInvoiceStatus": "Failed", "reason": "KeyError"})
    
    invoice_list = Invoice.objects.filter(customerName=customerName)
    
    if invoice_list.count() == 0:
        Invoice_ = Invoice(customerName=customerName, date=datetime.datetime.now())
        Invoice_.save()
        return Response({"createInvoiceStatus": "Success", "reason": "Null"})
    else:
        return Response({"createInvoiceStatus": "Failed", "reason": "InvoiceAlreadyExists"})
    
    
@api_view(['POST'])
def createInvoiceDetails(request):
    invoice_details_data = request.data 
    
    try:
        quantity = invoice_details_data['quantity']
        description = invoice_details_data['description']
        customerName = invoice_details_data['customerName']
        
    except KeyError:
        return Response({"createInvoiceDetailsStatus": "Failed", "reason": "KeyError"})
    
    matchedInvoices = Invoice.objects.filter(customerName=customerName)
    
    if matchedInvoices.count() == 0:
        return Response({"createInvoiceDetailsStatus": "Failed", "reason": "NoCustomerExistsCreateCustomerPlease"})
    elif matchedInvoices.count() == 1:
        invoice = matchedInvoices[0]
        InvoiceDetials_ = InvoiceDetails(quantity=quantity, description=description, invoice=invoice)
        InvoiceDetials_.save()
        return Response({"createInvoiceDetailsStatus": "Success", "reason": "Null"})
    else:
        return Response({"createInvoiceDetailsStatus": "Failed", "reason": "MultipleAccountError"})

@api_view(["POST"])
def updateInvoiceDetails(request):
    invoice_details_data = request.data 
    
    try:
        invoiceId = invoice_details_data['id']
        new_invoice_description = invoice_details_data['description']
        new_invoice_quantity = invoice_details_data['quantity']
        
    except KeyError:
        return Response({"updateInvoiceDetailsStatus": "Failed", "reason":"KeyError" })
    
    invoice_details_list = InvoiceDetails.objects.filter(id=invoiceId)
    
    if invoice_details_list.count() > 1:
       return Response({"updateInvoiceDetailsStatus": "Failed", "reason":"MultipleValues" })
    elif invoice_details_list.count() == 0:
        return Response({"updateInvoiceDetailsStatus": "Failed", "reason":"idDoesNotExist" })
    elif invoice_details_list.count() == 1:
        InvoiceDetail_ = invoice_details_list[0]
        InvoiceDetail_.description = new_invoice_description
        InvoiceDetail_.quantity = new_invoice_quantity
        InvoiceDetail_.save()
        return Response({"updateInvoiceDetailsStatus": "Sucess", "reason":"Null" })
        
        
    
    
             