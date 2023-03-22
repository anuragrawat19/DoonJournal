from django.shortcuts import render

# Create your views here.


def home(request):
    template = 'index.html'
    return render(request,template)

def about_us(request):
    template = 'about.html'
    return render(request,template)