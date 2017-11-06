from rest_framework import serializers
from .models import *


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'country', 'city', 'street', 'postalcode')

class ApiuserSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=True)
    class Meta:
        model = Apiuser
        fields = ('username', 'first_name', 'last_name', 'email', 'address', 'role')

    def update(self, instance, validated_data):
        instance.role = validated_data.pop('role')

        instance.save()
        return instance

class ShoppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shopping
        fields = ('invoice_id', 'item_id', 'user', 'quantity', 'date', 'address')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'item_name', 'price')
