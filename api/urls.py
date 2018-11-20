from django.urls import path
from .views import *
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
	path('<int:user_id>/profile/', ProfileView.as_view(), name='profile'),
    path('list/', ProductListView.as_view(), name='list'),
    path('<int:product_id>/detail/', ProductDetailView.as_view(), name='detail'),
]
