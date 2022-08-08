from dataclasses import field
from unittest import result
from urllib import request
from django.forms import JSONField
from rest_framework import serializers
from .models import *
from .gethost import hostlists
from .parsing import Parsing

#--------------------------플랜A--------------------------------------------------

# 입력값을 받아 알고리즘을 사용하여 계산 후 결과 값 json으로 출력
class ViruscountSerializer(serializers.Serializer):
   username = JSONField
   hostname = serializers.SerializerMethodField(method_name='getHostname')
   virus = serializers.SerializerMethodField(method_name='getVirusList')
   virus_sum = serializers.SerializerMethodField(method_name='countVirus')

   class Meta:
      model = Gethost
      fields = ('hostname','virus','virus_sum')

   def getHostname(self, obj):
      username = obj['username']
      viruslist = []
      hostlist = hostlists(username)
      return hostlist

   def getVirusList(self, obj):
      username = obj['username']
      viruslist = []
      virusarray = []
      hostlist = hostlists(username)
      for i in range(len(hostlist)):
         viruslist = Parsing(username, hostlist[i])
         virusarray.append(viruslist)
      return virusarray

   def countVirus(self, obj):
      username = obj['username']
      viruslist = []
      countlist = []
      hostlist = hostlists(username)
      for i in range(len(hostlist)):
         viruslist = Parsing(username, hostlist[i])
         countlist.append(len(viruslist))
      return countlist

#-----------------------------------------------------------------------



#---------------------플랜B----------------------------------------

# class ViruscountSerializer(serializers.Serializer):

#    class Meta:
#       model = Gethost
#       fields = ('username','virus','virus_sum')

#------------------------------------------------------------------