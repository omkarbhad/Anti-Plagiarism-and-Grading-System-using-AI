from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def graderesult(request):
    return render(request, "graderesult.html")


def validateresult(request):
    return render(request, "validateresult.html")


def both(request):
    return render(request, "both.html")
