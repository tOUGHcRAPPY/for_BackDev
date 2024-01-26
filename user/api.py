from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializers


class UserModelAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.AllowAny]

