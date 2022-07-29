from django.forms import JSONField
from rest_framework import serializers
from .models import *

class AddserverSerializer(serializers.Serializer):

   class Meta:
      model = Serveradd
      fields = ('username','servertype', 'servername')