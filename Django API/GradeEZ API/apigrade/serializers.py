from rest_framework import serializers
from .models import ApiGrade


class ApiGradeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiGrade
        fields = '__all__'
