from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
	dob = models.DateField(null=True, blank=True)
	number = models.CharField(max_length=8,null=True, blank=True)
	firstname = models.CharField(max_length=80, default=1)
	lastname = models.CharField(max_length=80, default=1)
	email = models.CharField(max_length=80, default=1)

	def __str__(self):
		return "ID:%s User:%s " % (self.id, self.user.username)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

#------------------------------------------------------#

class Product(models.Model):
	CATEGORY_CHOICE = (
		('MOBILES', 'MOBILES'),
		('TABLETS', 'TABLETS')
		)
	name = models.CharField(max_length=120)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=3)
	img = models.ImageField()
	quantity = models.PositiveIntegerField(default=0)
	category = models.CharField(max_length=20, default=0, choices=CATEGORY_CHOICE)

	def __str__(self):
		return self.name

class Address(models.Model):
	GOVERNORATE_CHOICE=(
	('Al Asimah', 'Al Asimah'),
	('Hawalli', 'Hawalli'),
	('Mubarak Al-Kabeer', 'Mubarak Al-Kabeer'),
	('Al-Ahmadi', 'Al-Ahmadi'),
	('Farwaniya', 'Farwaniya'),
	('Al-Jahra', 'Al-Jahra'),
	)
	user = models.ForeignKey(User, related_name='address',  on_delete=models.CASCADE)
	governorate = models.CharField(max_length=20, default=0, choices=GOVERNORATE_CHOICE)
	area = models.CharField(max_length=120)
	block = models.PositiveIntegerField(default=1)
	street = models.CharField(max_length=120)
	building_or_house = models.PositiveIntegerField(default=1)
	floor = models.PositiveIntegerField(default=0, blank=True, null=True)
	extra_directions = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.user.username



class Order(models.Model):
	STATUS_CHOICE=(
	('ORDERED', 'ORDERED'),
	('PACKED', 'PACKED'),
	('SHIPPED', 'SHIPPED'),
	('DELIVERED', 'DELIVERED')
	)

	price = models.FloatField(default=0)
	status = models.CharField(max_length=20, default='ORDERED', choices=STATUS_CHOICE)
	ordered_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orderedby")
	ordered_on = models.DateTimeField(auto_now_add = True)
	address = models.ForeignKey(Address,  on_delete=models.CASCADE, related_name="address", blank=True, null=True)


	def __str__(self):
		return self.ordered_by.username

#------------------------------------------------------#

class OrderProduct(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prod')
	quantity = models.PositiveIntegerField(default=0)
	order = models.ForeignKey(Order,related_name='order_product', on_delete=models.CASCADE)
	def __str__(self):
		return self.product.name


#------------------------------------------------------#
