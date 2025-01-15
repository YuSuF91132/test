from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    num = 10
    num2 = 10
    result = num + num2
    return HttpResponse(f"Результат {result}")

def news(request):
    return HttpResponse("Нет новостей")