
from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	DestroyAPIView,
	CreateAPIView,
)
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import *
from .permissions import *
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime

class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer

#------------------------------------------------------#

class ProductListView(ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductListSerializer
	permission_classes = [AllowAny,]
	filter_backends = [SearchFilter, OrderingFilter,]
	search_fields = ['name', 'description',]



class ProductDetailView(RetrieveAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'product_id'
	permission_classes = [AllowAny,]
#------------------------------------------------------#
class ProductCreateView(CreateAPIView):
	serializer_class = ProductListSerializer

class ProductDeleteView(DestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductListSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'product_id'

#------------------------------------------------------#

class ProfileCreateAPIView(CreateAPIView):
	serializer_class = ProfileSerializer

class ProfileView(RetrieveAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'user_id'
	permission_classes = [IsUser, ]
#------------------------------------------------------#Not needed now

# class ProfileUpdateView(RetrieveUpdateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     lookup_field = 'id'
#     lookup_url_kwarg = 'profile_id'

# class ProfileDeleteView(DestroyAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     lookup_field = 'id'
#     lookup_url_kwarg = 'profile_id'

#------------------------------------------------------#commented

# class OrderStatusListView(ListAPIView):
#     queryset = OrderStatus.objects.all()
#     serializer_class = OrderStatusListSerializer

class OrderDetailView(RetrieveAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderListSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'order_id'

class OrderCreateView(APIView):

	def post(self, request):
		new_order=Order.objects.create(
			ordered_by =request.user,
			ordered_on= "datetime.now()"
		)
		
		products=request.data
		print(request.data)
		for product in products:
			the_product = Product.objects.get(id=product["id"])
			new_order_product=OrderProduct(product=the_product, quantity=product["quantity"])
			new_order_product.order=new_order
			new_order_product.save()

		new_order.save()
		return Response(OrderSerializer)

		# serializer.save(user=self.request.user)

class OrderUpdateView(RetrieveUpdateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderCreateUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'order_id'

class OrderDeleteView(DestroyAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderListSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'order_id'

# class OrderTypeListView(ListAPIView):
#     queryset = OrderType.objects.all()
#     serializer_class = OrderTypeListSerializer

class OrderListView(ListAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderListSerializer













