from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Apiuser 
from .models import Address
from .models import Shopping
from .models import Item
from rest_framework.renderers import JSONRenderer
from api.serializers import *
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
import json
from rest_framework import permissions

import logging

class IsActiveUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        apiuser = getApiuser(request.user.id)
        if not user:
            return None
        return isProfileActive(apiuser)


class IsActiveOrWaitActivationUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        apiuser = getApiuser(request.user.id)
        if not user:
            return None
        return isProfileActive(apiuser)

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

# Create your views here.

@api_view(['POST'])
# @permission_classes((IsAuthenticated,))
def authenticate_user(request, format=None):
	username = request.data['username']
	password = request.data['password']
	user = authenticate(username=username, password=password)
	logging.warn(user)
	logging.warn(request)
	if not user:
		return HttpResponse(status=403)

	token = Token.objects.get(user=user)
	user = Apiuser.objects.get(username=user.username)
	if not user:
		return HttpResponse(status=404)

	return JSONResponse({ 'username': username, 'token': token.key, 'admin': user.role=='Admin' })

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def user_data(request, username):
	user = Apiuser.objects.get(username=username)
	apiuserSerialize = ApiuserSerializer(user).data

	return JSONResponse(apiuserSerialize)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def shopping(request, format=None):
	item_ids = request.data['item_id']
	quantities = request.data['quantity']
	address = request.data['address']
	user = Apiuser.objects.get(username=request.user.username, address=address)
	if not user:
		return HttpResponse(status=404)



	from time import gmtime, strftime
	request.data['date'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())


	import uuid
	invoice_id = str(uuid.uuid4())
	logging.warn(invoice_id)
	sumi = 0
	item_names = []
	for item_id, quantity in zip(item_ids, quantities):
		d = ({ 'address': address,
			'quantity': quantity,
		  	'user': int(user.id),
		  	'item_id': item_id,
		  	'invoice_id': invoice_id})
		item = Item.objects.get(id=item_id)
		sumi += item.price * quantity
		item_names.append(item.item_name)
		shoppingserializer = ShoppingSerializer(data=d)
		if not shoppingserializer.is_valid():
			logging.warn(shoppingserializer.errors)
			return HttpResponse(shoppingserializer.errors, status=404)

		shoppingserializer.save()

	invoice = {
		'id':  invoice_id,
		'items': item_names,
		'quantity': quantities,
		'date' : request.data['date'],
		'sum': sumi,
		'address': AddressSerializer(Address.objects.get(id=address)).data,
	}

	return JSONResponse(invoice)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_user_invoice(request):
	user = Apiuser.objects.get(username=request.user.username)
	logging.warn(Shopping.objects.filter(user=user))
	logging.warn('==================')
	# shoppings = ShoppingSerializer(Shopping.objects.filter(user=user), many=True).data
	shoppings = Shopping.objects.filter(user=user)
	invoices_data = []
	d = {}
	for shopping in shoppings:
		item = shopping.item_id
		item_name = item.item_name
		item_price = item.price

		if shopping.invoice_id in d:
			d[shopping.invoice_id]['items'].append(item_name)
			d[shopping.invoice_id]['quantity'].append(shopping.quantity)
			d[shopping.invoice_id]['sum'] += item_price * shopping.quantity
		else:
			address = shopping.address
			date = shopping.date
			qqt = shopping.quantity
			d[shopping.invoice_id] = ({
										'id' : shopping.invoice_id,
										'user': user.username,
										'date': date,
										'address': AddressSerializer(address).data,
										'items' : [item_name],
										'quantity': [qqt],
										'sum': item_price * qqt
									})

	for idi in d:
		invoices_data.append(d[idi])
	
	return JSONResponse(invoices_data)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def users_data_all(request):
	user = Apiuser.objects.get(username=request.user.username)
	if not user:
		return HttpResponse(status=404)
	if user.role != 'Admin':
		return HttpResponse(status=403)

	users = Apiuser.objects.all()

	logging.warn(users)
	apiuserSerializer = ApiuserSerializer(users, many=True)



	result = {
		'users_data': apiuserSerializer.data,
		'roles': Apiuser._meta.get_field('role').choices
	}

	return JSONResponse(result)

@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def update_user(request):
	logging.warn('update user')
	request_user = request.user
	request_users_data_all = request.data

	logging.warn(request_users_data_all)
	for user_data in request_users_data_all:
		user = Apiuser.objects.get(username=user_data['username'])
		apiuserSerializer = ApiuserSerializer(user, user_data)
		if not apiuserSerializer.is_valid():
			return Response(apiuserSerializer.errors)
		apiuserSerializer.save()

	return HttpResponse(status=200)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def loaditems(request):
 	items = Item.objects.all()
 	itemSerializer = ItemSerializer(items, many=True)

 	return JSONResponse(itemSerializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def address(request, format=None):
	country = request.data['country']
	city = request.data['city']
	street = request.data['street']
	postalcode = request.data['postalcode']

	logging.warn(request.user)

	# a = Address.objects.create(country=country, city=city, street=street, postalcode=postalcode)
	addressSerializer = AddressSerializer(data=request.data)
	if not addressSerializer.is_valid():
		return Response(addressSerializer.errors)

	a = addressSerializer.save()

	user = Apiuser.objects.get(username=request.user.username)
	user.address.add(a.id)
	user.save()

	return HttpResponse(status=200)

@api_view(['POST'])
# @permission_classes((IsAuthenticated,))
def signup(request, format=None):
	firstname = request.data['firstname']
	lastname = request.data['lastname']
	email = request.data['email']
	password = request.data['password']
	confirmpassword = request.data['confirmpassword']
	username = request.data['username']

	if confirmpassword != password:
		return HttpResponse('the password should match', status=400)

	try:
		user = User.objects.get(username=username)
		return HttpResponse('username already exists', status=403) # user already exists
	except User.DoesNotExist:
		user = User.objects.create_user(username=username, password=password, email=email)
		b = Apiuser.objects.create(first_name=firstname, last_name=lastname, email=email, password=password, username=username)

	return HttpResponse(status=200)

