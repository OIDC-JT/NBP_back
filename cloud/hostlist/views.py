from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import views
from .serializers import *

class hoslistView(APIView):
    def get(self, request):
        username = request.user.username
        serializer = GethostSerializer(username)

        return Response(serializer.data)