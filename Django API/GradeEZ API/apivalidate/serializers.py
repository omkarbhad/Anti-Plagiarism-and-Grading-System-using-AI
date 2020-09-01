from rest_framework import serializers
from .models import ApiValidate


class ApiValidateSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiValidate
        fields = '__all__'
