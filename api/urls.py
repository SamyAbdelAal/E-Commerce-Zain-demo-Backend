from django.urls import path
from .views import *
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
	path('<int:user_id>/profile/', ProfileView.as_view(), name='profile'),
    path('list/product/', ProductListView.as_view(), name='product-list'),
    path('<int:product_id>/detail/product/', ProductDetailView.as_view(), name='product-detail'),
    path('create/order/', OrderCreateView.as_view(), name='order-create'),
    path('list/order/', OrderListView.as_view(), name='order-list'),
    path('<int:product_id>/detail/order/', OrderDetailView.as_view(), name='order-detail'),




]
