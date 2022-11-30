from django.urls import path

from . import views


from django.contrib.admin.views.decorators import staff_member_required
app_name = 'products'
urlpatterns = [
  path('', views.ProductListView.as_view(), name='index'),
  path('<pk>/delete/', views.ProductDeleteView.as_view(), name='delete'),
  path('create/', views.ProductCreateView.as_view(), name='create'),
  path('<pk>/update', staff_member_required(views.ProductUpdateView.as_view()), name='update')
]