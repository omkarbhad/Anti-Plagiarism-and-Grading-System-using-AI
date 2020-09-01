from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('graderesult/',views.graderesult,name="graderesult"),
    path('validateresult/',views.validateresult,name="validateresult"),
    path('both/', views.both, name="both"),
    path('admin/', admin.site.urls),
    path('grade/', include('apigrade.urls')),
    path('validate/', include('apivalidate.urls'))
]
