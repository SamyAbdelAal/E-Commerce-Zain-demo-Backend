from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserCreateSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['username', 'password',]

	def create(self, validated_data):
		new_user=User.objects.create(
			username = validated_data['username'],
			password = validated_data['password'],
			#email = validated_data['email'],
			#first_name = validated_data['first_name'],
			#last_name = validated_data['last_name'],

		)
		
		new_user.set_password(validated_data['password'])
		new_user.save()
		return validated_data

class ProfileSerializer(serializers.ModelSerializer):
	email = serializers.SerializerMethodField()
	name = serializers.SerializerMethodField()

	class Meta:
		model = Profile
		fields = ['dob', 'firstname', 'lastname', 'email', 'profile_pic', 'number']

	# def get_email(self, obj):
	# 	return (obj.user.email)

	# def get_name(self, obj):
	# 	return "%s %s"%(obj.user.first_name, obj.user.last_name)
		
#------------------------------------------------------#

class ProductListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ['id',
		'name',
		'price',
		'category',
		'img',
			]

class ProductDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ['id',
		'name',
		'price',
		'description',
		'category',
		'img', 'quantity'
			]

#------------------------------------------------------#

class AddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address
		fields = ['id', 'user', 'governorate', 'area', 'block', 'street', 'building_or_house', 'floor', 'extra_directions']



class OrderProductSerializer(serializers.ModelSerializer):
	name = serializers.SerializerMethodField()
	class Meta:
		model = OrderProduct
		fields = ['name','quantity']
	def get_name(self, obj):
		return obj.product.name

class OrderSerializer(serializers.ModelSerializer):
	address= AddressSerializer( read_only=True)

	class Meta:
		model = Order
		fields = ['id', 'ordered_by', 'ordered_on', 'status', 'address']

class OrderListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = ['id', 'ordered_on', 'status', 'address']

class OrderDetailSerializer(serializers.ModelSerializer):
	order_product= OrderProductSerializer(many=True, read_only=True)
	address= AddressSerializer(read_only=True)
	class Meta:
		model = Order
		fields = ['id', 'ordered_by', 'ordered_on', 'status', 'address','order_product' ]

#------------------------------------------------------#

	# def get_products(self, obj):
	# 	products = OrderProduct.objects.filter(order=obj)
	# 	# print(products)
	# 	product_list=[]
	# 	for product in products:
			
	# 		product_list.append(OrderProductSerializer(product, many=True).data)
	# 	# return OrderProductSerializer(products, many=True).data
	# 	print(product_list)
	# 	return product_list

#------------------------------------------------------#



# class AddressCreateUpdateSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Address
# 		fields = ['id', 'user', 'governorate', 'area', 'block', 'street', 'building_or_house', 'floor', 'extra_directions']



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


# class OrderCreateUpdateSerializer(serializers.ModelSerializer):

# 	class Meta:
# 		model = Order
# 		fields = ['id','ordered_on', 'product','status', 'ordered_by',]




