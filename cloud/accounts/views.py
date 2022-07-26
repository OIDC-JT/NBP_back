from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers
from accounts.models import User
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AddsqlView(APIView):
    def post(self, request):
        username = request.user.username
        serializer = AutosqlSerializer(username)

        return Response(serializer.data)