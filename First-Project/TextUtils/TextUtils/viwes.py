# i have created this file - Jay

from django.http import HttpResponse


def index(request):
    return HttpResponse('''<h1>Hello, welcome to TextUtils!</h1>
                        <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">Django Course</a>''')

def about(request):
    return HttpResponse("This is the about page of TextUtils.")