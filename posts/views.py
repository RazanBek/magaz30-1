from django.shortcuts import HttpResponse
from datetime import datetime

# Create your views here.


def hello_view(request):
    if request.method == "GET":
        return HttpResponse("Hello! Its my project")


def now_date_view(request):
    now = datetime.now()
    current_date = now.strftime("%d-%m-%Y")
    if request.method == "GET":
        return HttpResponse(f"Дата:{current_date}")


def goodby_view(request):
    if request.method == "GET":
        return HttpResponse('Goodby user!')
