from dataclasses import field
from unittest import result
from django.forms import JSONField
from rest_framework import serializers
from .models import *
from .crawling_return import NBP

# 입력값을 받아 알고리즘을 사용하여 계산 후 결과 값 json으로 출력
class CalculateSerializer(serializers.Serializer):
   inputs = JSONField
   results = serializers.SerializerMethodField(method_name='calculateResult')

   class Meta:
      model = useNBP
      fields = ('inputs','results')

   def calculateResult(self, obj):
      nums = obj['list']
      return NBP(nums)
