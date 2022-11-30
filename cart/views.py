# Create your views here.
from cart.cart import Cart
from products.models import Product
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
import mercadopago
from django.views.decorators.csrf import csrf_exempt


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
    return HttpResponseRedirect(reverse('cart:cart'))

def remove_from_cart(request, pk):
    product = Product.objects.get(id=pk)
    cart = Cart(request)
    cart.remove(product)
    return HttpResponseRedirect(reverse('cart:cart'))

def get_cart(request):
    return render(request, 'cart/cart.html', {'cart': Cart(request)})

def generate_payment(request):
    return render(request, 'cart/generate_payment.html', {'cart': Cart(request)})

@csrf_exempt
def process_payment(request):
    sdk = mercadopago.SDK("APP_USR-2180497889937881-112909-4d49264e0c5960400250cb46b4c39a4e-1125665108")
    request_values = json.loads(request.body)
    payment_data = {
        "transaction_amount": float(request_values["transaction_amount"]),
        "token": request_values["token"],
        "installments": int(request_values["installments"]),
        "payment_method_id": request_values["payment_method_id"],
        "issuer_id": request_values["issuer_id"],
        "payer": {
            "email": request_values["payer"]["email"],
            "identification": {
                "type": request_values["payer"]["identification"]["type"], 
                "number": request_values["payer"]["identification"]["number"]
            }
        }
    }

    payment_response = sdk.payment().create(payment_data)
    payment = payment_response["response"]

    print("status =>", payment["status"])
    print("status_detail =>", payment["status_detail"])
    print("id =>", payment["id"])
    if payment["id"] == "approved":
        Cart(request).clear()
        return HttpResponseRedirect(reverse('cart:cart'))
    return render(request, 'cart/cart.html', {'cart': Cart(request)})