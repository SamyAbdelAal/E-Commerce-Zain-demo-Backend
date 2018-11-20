from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Product(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=3)
	img = models.ImageField()

	def __str__(self):
		return self.name

class Profile(models.Model):
	user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
	dob = models.DateField(null=True, blank=True)
	profile_pic = models.ImageField(default="/profile_pic/pic placeholder.png/",upload_to='profile_pic', null=True, blank=True)
	
	def __str__(self):
		return "ID:%s User:%s " % (self.id, self.user.username)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()