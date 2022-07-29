from dataclasses import field
from unittest import result
from django.forms import JSONField
from rest_framework import serializers
from .models import *
from .gethost import hostlists

# 입력값을 받아 알고리즘을 사용하여 계산 후 결과 값 json으로 출력
class GethostSerializer(serializers.Serializer):
   lists = serializers.SerializerMethodField(method_name='getHostList')

   class Meta:
      model = Gethost
      fields = ('lists')

   def getHostList(self, obj):
      nums = obj
      return hostlists(nums)
