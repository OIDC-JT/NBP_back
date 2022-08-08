from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import views
from .serializers import *
from .gethost import hostlists
from .parsing import Parsing
import json

#-----------------플랜A----------------------------------------------

class viruslistView(APIView):
    def post(self, request):
        
        username = request.data
        serializer = ViruscountSerializer(username)

        return Response(serializer.data)

#-------------------------------------------------------------------



#-----------------플랜B--------------------------------------------
# class viruslistView(APIView):
#     def post(self, request):
#         data = []
#         username = request.data
#         hostlist = hostlists(username)
#         for host in hostlist:
#             data.append({
#                 "hostname" : host,
#                 "virus" : Parsing(username, host),
#                 "virus_sum" : len(Parsing(username,host))
#             })
#         return Response(data)
#-----------------------------------------------------------------------