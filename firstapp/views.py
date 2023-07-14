from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request , 'firstapp/index.html')


def details(request):
    return render(request , 'firstapp/details.html')