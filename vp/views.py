from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def packages(request):
    return render(request, 'packages.html')

def career(request):
    return render(request, 'career.html')

def news(request):
    return render(request, 'news.html')
