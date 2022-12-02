from django.shortcuts import render
from cart.models import Order
from django.views.generic.edit import UpdateView
def my_orders(request):
  user_id = request.user.id
  my_orders = Order.objects.filter(buyer_id=user_id).all()
  print(my_orders)
  return render(request, 'orders/my_orders.html', context={ 'orders': my_orders })

def all_orders(request):
  all_orders = Order.objects.all()
  return render(request, 'orders/all_orders.html', context={'orders': all_orders})

class OrderUpdateView(UpdateView):
  model = Order
  fields = ['pago','entregue']
  success_url = "/orders/"