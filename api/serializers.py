from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserCreateSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['username', 'email', 'password', 'first_name', 'last_name']

	def create(self, validated_data):
		new_user=User.objects.create(
			username = validated_data['username'],
			password = validated_data['password'],
			email = validated_data['email'],
			first_name = validated_data['first_name'],
			last_name = validated_data['last_name'],

		)
		
		new_user.set_password(validated_data['password'])
		new_user.save()
		return validated_data


class ProfileSerializer(serializers.ModelSerializer):
	email = serializers.SerializerMethodField()
	name = serializers.SerializerMethodField()

	class Meta:
		model = Profile
		fields = ['name', 'dob', 'email', 'profile_pic']

	def get_email(self, obj):
		return (obj.user.email)

	def get_name(self, obj):
		return "%s %s"%(obj.user.first_name, obj.user.last_name)
		


class ProductListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ['id',
		'name',
		'price',
		'img',
			]


class ProductDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ['id',
		'name',
		'price',
		'description',
		'img', 'quantity'
			]

class OrderProductSerializer(serializers.ModelSerializer):
	name = serializers.SerializerMethodField()
	class Meta:
		model = OrderProduct
		fields = ['name','quantity']
	def get_name(self, obj):
		return obj.product.name

class OrderSerializer(serializers.ModelSerializer):
	# status = OrderStatusListSerializer()
	class Meta:
		model = Order
		fields = ['id','ordered_by' ]
#dashboard----------------------
# class UserListSerializer(serializers.ModelSerializer):
# 	profile = ProfileSerializer()
# 	orders = serializers.SerializerMethodField()
# 	products = serializers.SerializerMethodField()

# 	class Meta:
# 		model = User
# 		fields = ['id','first_name','last_name','username','email','profile', 'orders', 'products']

# 	def get_orders(self, obj):
# 		orders = obj.orderedby.all()
# 		return UserOrderListSerializer(orders, many=True).data

# 	def get_products(self, obj):
# 		products = obj.product_set.all()
# 		return ProductListSerializer(products, many=True).data

class OrderCreateUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Order
		fields = ['id','ordered_on','updated_on','price', 'product','status', 'ordered_by', 'updated_by','orderNumber']

# class OrderStatusListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderStatus
#         fields = '__all__'

# class OrderTypeListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderType
#         fields = '__all__'

# class OrderNumberListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderNumber
#         fields = '__all__'

class UserOrderListSerializer(serializers.ModelSerializer):
	# status = OrderStatusListSerializer()
	class Meta:
		model = Order
		fields = ['id','ordered_on','status' ]

class OrderListSerializer(serializers.ModelSerializer):
	# ordered_by = UserListSerializer()
	# status = OrderStatusListSerializer()
	products = serializers.SerializerMethodField()
	# orderNumber = OrderNumberListSerializer(many=True)

	class Meta:
		model = Order
		fields = ['id','ordered_on','updated_on','status','products','price', 'ordered_by', 'orderNumber' ]

	def get_products(self, obj):
		products = obj.orderProduct_set.all()
		return UserOrderSerializer(products, many=True).data

class UserOrderDetailSerializer(serializers.ModelSerializer):
	product=serializers.SerializerMethodField()
	class Meta:
		model = Order
		fields = ['id','ordered_on','updated_on','price','status', 'ordered_by', 'updated_by','orderNumber' ]

	def get_products(self, obj):
		products = obj.orderProduct_set.all()
		return UserOrderSerializer(products, many=True).data
