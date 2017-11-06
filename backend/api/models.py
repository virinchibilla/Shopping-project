from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from datetime import datetime


# for user in User.objects.all():
#    Token.objects.get_or_create(user=user)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Address(models.Model):
	country = models.CharField(max_length=120)
	city = models.CharField(max_length=120)
	street = models.CharField(max_length=120)
	postalcode = models.CharField(max_length=120)


	"""docstring for ClassName"""
	def __str__(self):
		return "%s %s %s %s" % (self.country, self.city, self.street, self.postalcode)


# Create your models here.
class Apiuser(models.Model):
	username = models.CharField(max_length=120, unique=True)
	first_name = models.CharField(max_length=120)
	last_name = models.CharField(max_length=120)
	password = models.CharField(max_length=120)
	email = models.EmailField(max_length=30, unique=True)
	address = models.ManyToManyField(Address, blank=True)
	
	ROLE = (
		('Customer','customer'),
		('Sales person','sales person'),
		('Manager','manager'),
		('Admin','admin'),
		('User','user')
		)

	role = models.CharField(
		max_length=30,
		choices = ROLE,
		default = 'User'
		)

	is_active = models.BooleanField(default=False)

	"""docstring for ClassName"""
	def __str__(self):
		return self.username


class Item(models.Model):
	item_name = models.CharField(max_length=120)
	price = models.IntegerField()
	
	"""docstring for ClassName"""
	def __str__(self):
		return self.item_name

class Shopping(models.Model):
	invoice_id = models.CharField(max_length=64)
	item_id = models.ForeignKey(Item)
	user = models.ForeignKey(Apiuser)
	quantity= models.IntegerField()
	date = models.DateTimeField(default=datetime.now, blank=True)
	address = models.ForeignKey(Address)
	
	"""docstring for ClassName"""
	def __str__(self):
		return self.invoice_id


