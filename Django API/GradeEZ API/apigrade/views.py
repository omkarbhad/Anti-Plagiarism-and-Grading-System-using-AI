from rest_framework import viewsets
from rest_framework.response import Response
from . import grade_ml
from .models import ApiGrade
from .serializers import ApiGradeSerializers


class ApiGradeView(viewsets.ModelViewSet):
    queryset = ApiGrade.objects.order_by("-id")
    serializer_class = ApiGradeSerializers

    def create(self, request, *args, **kwargs):
        viewsets.ModelViewSet.create(self, request, *args, **kwargs)
        json_object = ApiGrade.objects.latest("id")
        grade = grade_ml.predict_grade(json_object.string, json_object.custom_marks)
        return Response({"grade": grade[0]})
