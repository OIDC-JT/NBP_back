from rest_framework import serializers
from .models import *
from .autosql import autosql

# 입력값을 받아 알고리즘을 사용하여 계산 후 결과 값 json으로 출력
class AutosqlSerializer(serializers.Serializer):
   results = serializers.SerializerMethodField(method_name='autoaddsql')

   class Meta:
      model = Autosql
      fields = ('username','results')

   def autoaddsql(self, obj):
      username = obj
      return autosql(username)
