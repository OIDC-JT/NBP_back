from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import serializers
from accounts.models import User
from .serializers import *
from rest_framework.response import Response
from .securitybat import Security_batch
# Create your views here.

class SecuritybatchView(APIView):
    def post(self, request):
        username = request.user.username
        servertype = request.data.get('servertype')
        servername = request.data.get('servername')
        Security_batch(username, servertype, servername)
        serializer = AddsecuritySerializer(request.data)

        return Response(serializer.data)