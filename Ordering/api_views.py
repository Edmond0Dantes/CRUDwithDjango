from . import serializers
from . import  models
from rest_framework.views import APIView
from rest_framework import  status
from rest_framework.response import Response


class UserCreateList(APIView):


    def get(self, request,format=None):

        queryset = models.User.objects.all()

        serializer = serializers.UserSerializer(queryset, many=True)

        return Response(serializer.data)


    def post(self,request,format=None):

        serializer=serializers.UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data,status=status.HTTP_201_CREATED)


class UserUpdateDelete(APIView):

    def get(self,request,pk,format=None):

        user=models.User.objects.get(pk  =  pk)

        serializer=serializers.UserSerializer(user)

        return Response(serializer.data)


    def delete(self,request,pk,format=None):

        user=models.User.objects.get(pk  =  pk)

        user.delete()

        return Response("user removed",status=status.HTTP_204_NO_CONTENT)


    def put(self,request,pk,format=None):

        user=models.User.objects.get(pk  =  pk)

        serializer=serializers.UserSerializer(user,data=request.data)

        if(serializer.is_valid()):

                serializer.save()

                return Response(serializer.data)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class OrderUpdateDelete(APIView):

    def get(self,request,pk,format=None):

        order=models.Order.objects.get(pk=pk)

        serializer=serializers.RecordSerializer(order)

        return Response(serializer.data)


    def delete(self,request,pk,format=None):

        order=models.Order.objects.get(pk=pk)

        order.delete()

        return Response("order removed", status=status.HTTP_204_NO_CONTENT)


    def put(self,request,pk,format=None):

        order=models.Order.objects.get(pk= pk)

        serializer=serializers.RecordSerializer(order,data=request.data)

        if(serializer.is_valid()):

                serializer.save()

                return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderCreateList(APIView):


    def get(self, request, format=None):

        queryset = models.Order.objects.all()

        serializer = serializers.RecordSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):

        order=serializers.RecordSerializer(data=request.data)

        order.is_valid(raise_exception=True)

        order.save()

        return Response(order.data, status=status.HTTP_201_CREATED)



















