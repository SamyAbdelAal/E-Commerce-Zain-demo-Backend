from django.urls import path
from .views import *
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
	path('profile/<int:user_id>/', ProfileView.as_view(), name='profile'),
    path('product/list/', ProductListView.as_view(), name='product-list'),
    path('product/<int:product_id>/detail/', ProductDetailView.as_view(), name='product-detail'),
    path('order/create/', OrderCreateView.as_view(), name='order-create'),
    path('order/list/', OrderListView.as_view(), name='order-list'),
    path('order/<int:order_id>/detail/', OrderDetailView.as_view(), name='order-detail'),
    path('address/create/', AddressCreateView.as_view(), name='address'),
    path('address/list/', AddressListView.as_view(), name='address_list'),

]
