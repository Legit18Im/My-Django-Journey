# i have created this file - Jay

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, welcome to TextUtils!")

def about(request):
    return HttpResponse("This is the about page of TextUtils.")