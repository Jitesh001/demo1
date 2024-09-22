from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World!")

def devHome(request):
    return HttpResponse("Hello, Dev World!")
