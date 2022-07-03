from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import views
from .serializers import *

class NbpView(APIView):
    def post(self, request):
        inputnbp = request.data
        serializer = CalculateSerializer(inputnbp)

        return Response(serializer.data)