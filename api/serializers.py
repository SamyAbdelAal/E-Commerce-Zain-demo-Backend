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
		'img',
			]

