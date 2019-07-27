from rest_framework import serializers
from django.core.validators import  validate_email
from .models import Order,User


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model=User
        fields=(
                'name',
                'phone',
                'email',
                'address',
                )


    def validate_phone(self, attrs):

        if(attrs[0:2]=="09"):
            if(len(attrs)==11):
                return attrs
        raise serializers.ValidationError("wrong phone number")


    def validate_email(self, attrs):

        try:
            validate_email(attrs)
            return attrs
        except:
            raise serializers.ValidationError("wrong Email")



class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=(
                'user',
                'datetime',
                'purchase',
                'purchase_id',
                )