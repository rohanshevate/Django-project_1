from django.shortcuts import *

# Create your views here.
def home(request):
    return HttpResponse("Hi")