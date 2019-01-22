from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserCreateSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['username', 'password']

	def create(self, validated_data):
		new_user=User.objects.create(
			username = validated_data['username'],
			password = validated_data['password'],
		)

		new_user.set_password(validated_data['password'])
		new_user.save()
		return validated_data

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = [ 'firstname', 'lastname', 'dob', 'email', 'number']

#------------------------------------------------------#Product

class ProductListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ['id',
		'name',
		'description',
		'price',
		'category',
		'img',
		"category"
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

#------------------------------------------------------#Address

class AddressSerializer(serializers.ModelSerializer):
	user = serializers.PrimaryKeyRelatedField(read_only=True)
	class Meta:
		model = Address
		fields = '__all__'

#------------------------------------------------------#Order

class OrderProductSerializer(serializers.ModelSerializer):
	name = serializers.SerializerMethodField()
	price = serializers.SerializerMethodField()
	class Meta:
		model = OrderProduct
		fields = ['id','name','quantity','price']
	def get_name(self, obj):
		return obj.product.name
	def get_price(self, obj):
		return obj.product.price

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
		fields = ['id', 'ordered_by', 'ordered_on', 'status', 'address','order_product','price' ]

#------------------------------------------------------#
