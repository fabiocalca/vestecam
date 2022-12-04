from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from . import views
app_name = 'orders'

urlpatterns = [
    path('', login_required(views.my_orders), name='my_orders'),
    path('all_orders', staff_member_required(views.all_orders), name='all_orders'),
    path('<pk>/update', staff_member_required(views.OrderUpdateView.as_view()), name='update'),
    path('<pk>/delete', staff_member_required(views.OrderDeleteView.as_view()), name='delete'),
]