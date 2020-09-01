from rest_framework import viewsets
from rest_framework.response import Response
from . import validation_ml
from .models import ApiValidate
from .serializers import ApiValidateSerializers


class ApiValidateView(viewsets.ModelViewSet):
    queryset = ApiValidate.objects.order_by("-id")
    serializer_class = ApiValidateSerializers

    def create(self, request, *args, **kwargs):
        if request.method == 'POST':
            viewsets.ModelViewSet.create(self, request, *args, **kwargs)
            json_object = ApiValidate.objects.latest("id")
            validate = validation_ml.detect(json_object.string)

            return Response(validate)
