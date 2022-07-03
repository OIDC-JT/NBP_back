from dataclasses import field
from unittest import result
from django.forms import JSONField
from rest_framework import serializers
from .models import *
from .crawling_return import NBP

class CalculateSerializer(serializers.Serializer):
   inputs = JSONField
   results = serializers.SerializerMethodField(method_name='calculateResult')

   class Meta:
      model = useNBP
      fields = ('inputs','results')

   def calculateResult(self, obj):
      nums = obj['list']
      return NBP(nums)
