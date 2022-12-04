from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'cart'
urlpatterns = [
  path('<pk>/add_to_cart/', views.add_to_cart, name='add_to_cart'),
  path('<pk>/remove_from_cart/', views.remove_from_cart, name = 'remove_from_cart'),
  path('', views.get_cart, name='cart'),
  path('generate_payment/', login_required(views.generate_payment), name='generate_payment'),
  path('payment_method', login_required(views.payment_method), name='payment_method'),
]