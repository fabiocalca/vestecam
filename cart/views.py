# Create your views here.
from cart.cart import Cart
from products.models import Product
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
import mercadopago
from django.views.decorators.csrf import csrf_exempt
from . import models
from django.contrib.auth.models import User
import json

def add_to_cart(request, pk):
    product = Product.objects.get(id=pk)
    cart = Cart(request)
    if product.desconto:
      valor = product.valor_com_desconto
    else:
        valor = product.valor
    cart.add(product, valor, quantity=1)
    print(cart.summary())
    return HttpResponseRedirect(reverse('products:index'))

def remove_from_cart(request, pk):
    product = Product.objects.get(id=pk)
    cart = Cart(request)
    cart.remove(product)
    return HttpResponseRedirect(reverse('cart:cart'))

def get_cart(request):
    return render(request, 'cart/cart.html', {'cart': Cart(request)})

def generate_payment(request):
    return render(request, 'cart/generate_payment.html', {'cart': Cart(request)})

def payment_method(request):
    items = ''
    for i in Cart(request):
        items += (str(i.quantity) + 'x ' + str(i.product.nome) + '\n')
    return render(request, 'cart/payment_method.html', {'cart': Cart(request), 'items': items})

@csrf_exempt
def process_payment(request):

    sdk = mercadopago.SDK("APP_USR-2180497889937881-112909-4d49264e0c5960400250cb46b4c39a4e-1125665108")
    payment_data = {
   "transaction_amount": float(request.POST.get("transactionAmount")),
    "description": request.POST.get("productDescription"),
    "payment_method_id": "pix",
    "payer": {
        "email": "test@test.com",
        "first_name": request.POST.get("payerFirstName"),
        "last_name": request.POST.get("payerLastName"),
        "identification": {
            "type": "CPF",
            "number": request.POST.get("docNumber")
        },
        "address": {
            "zip_code": "06233-200",
            "street_name": "Av. das Nações Unidas",
            "street_number": "3003",
            "neighborhood": "Bonfim",
            "city": "Osasco",
            "federal_unit": "SP"
        }
    }
}
    
    payment_response = sdk.payment().create(payment_data)
    payment = payment_response["response"]
    print("status =>", payment["status"])
    print("status_detail =>", payment["status_detail"])
    print("id =>", payment["id"])
    items = ''
    for i in Cart(request):
        items += (str(i.quantity) + 'x ' + str(i.product.nome) + '\n')
    user_id = request.user.id
    valor = Cart(request).summary()
    payment_link = payment["point_of_interaction"]["transaction_data"]["ticket_url"]
    order_obj = models.Order(buyer=User.objects.get(id=user_id), payer_name=(request.POST.get("payerFirstName")), payer_phone=request.POST.get("payerPhone"), payment_id=payment["id"], payment_status=payment["status"], payment_link=payment_link, valor=valor, items=items)
    order_obj.save()
    Cart(request).new(request)
    return render(request, 'cart/payment.html', {'payment': payment})