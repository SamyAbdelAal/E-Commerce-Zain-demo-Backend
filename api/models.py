from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
	dob = models.DateField(null=True, blank=True)
	profile_pic = models.ImageField(upload_to='profile_pic', null=True, blank=True)
	
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
	name = models.CharField(max_length=120)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=3)
	img = models.ImageField()
	quantity = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.name


#------------------------------------------------------#		

# class OrderStatus(models.Model):
# 	name = models.CharField(max_length=200)

# 	def __str__(self):
# 		return self.name

# class OrderType(models.Model):
# 	name = models.CharField(max_length=200)

# 	def __str__(self):
# 		return self.name

# class OrderNumber(models.Model):
# 	number = models.IntegerField()

# 	def __str__(self):
# 		return self.number

class Order(models.Model):
	# status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
	# price = models.FloatField(default=0)
	ordered_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orderedby")
	# updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updatedby")
	# ordered_on = models.DateTimeField(auto_now_add = True)
	ordered_on = models.TextField()
	# updated_on = models.DateTimeField(auto_now = True)
	# order_number = models.ManyToManyField(OrderNumber, blank=True)
	

#------------------------------------------------------#

class OrderProduct(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=0)
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	def __str__(self):
		return self.product.name



