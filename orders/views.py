
from django.shortcuts import render
from cart.models import Order
from django.views.generic.edit import UpdateView, DeleteView
import requests
from django.db.models import F
from django.utils.functional import keep_lazy
headers = headers = {
    'Authorization': 'Bearer APP_USR-2180497889937881-112909-4d49264e0c5960400250cb46b4c39a4e-1125665108',
  }
'''
def my_orders(request):
  user_id = request.user.id
  my_orders = Order.objects.filter(buyer_id=user_id).all()
  my_ids = my_orders.values('payment_id')
  for order in my_orders:
    response = requests.get('https://api.mercadopago.com/v1/payments/'+str(order.payment_id), headers=headers).json()
    if F('payment_status') != response["status"]:
      Order.objects.filter(payment_id=order.payment_id).update(payment_status=response["status"])
  return render(request, 'orders/my_orders.html', context={ 'orders': my_orders })
'''

def my_orders(request):
  user_id = request.user.id
  my_orders = Order.objects.filter(buyer_id=user_id).all()
  for order in my_orders:
    response = requests.get('https://api.mercadopago.com/v1/payments/'+str(order.payment_id), headers=headers).json()
    order.payment_status = response["status"]
  Order.objects.bulk_update(my_orders, ['payment_status'], batch_size=500)
  return render(request, 'orders/my_orders.html', context={ 'orders': my_orders })


def all_orders(request):
  all_orders = Order.objects.all()
  for order in all_orders:
    response = requests.get('https://api.mercadopago.com/v1/payments/'+str(order.payment_id), headers=headers).json()
    if order.payment_status != response["status"]:
      Order.objects.filter(payment_id=order.payment_id).update(payment_status=response["status"])
  return render(request, 'orders/all_orders.html', context={'orders': all_orders})

class OrderUpdateView(UpdateView):
  model = Order
  fields = ['entregue']
  success_url = "/orders/"

class OrderDeleteView(DeleteView):
  model = Order
  success_url ="/orders/all_orders"
  template_name = "orders/delete_confirm.html"