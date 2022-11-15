from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    def create(self,request,*args,**kwargs):
        serializer =  self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token,created = Token.objects.get_or_create(user=serializer.instance)
        return Response(
            {'token':token.key},status=status.HTTP_201_CREATED
        )
    def list(self,request,*args,**kwargs):
        response = {'message':"You cann't create list to users"}
        Response(response,status=status.HTTP_400_BAD_REQUEST)
        
    def update(self,request,*args,**kwargs):
        response = {'message':"You cann't update user"}
        Response(response,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,*args,**kwargs):
        response = {'message':"You cann't delete user"}
        Response(response,status=status.HTTP_400_BAD_REQUEST)
