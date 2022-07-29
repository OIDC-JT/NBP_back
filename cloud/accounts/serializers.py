from rest_framework import serializers
from .models import *
from .autosql import autosql

# 입력값을 받아 알고리즘을 사용하여 계산 후 결과 값 json으로 출력
class AutosqlSerializer(serializers.Serializer):

   class Meta:
      model = Autosql
      fields = ('username')
