from django.shortcuts import render, HttpResponse
from datetime import datetime
from vp.models import Form, Footer

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        form = Form(name=name, email=email, subject=subject, message=message, date=datetime.today())
        form.save()
    return render(request, 'index.html')
        
def footer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        footer = Footer(name=name, email=email, message=message, date=datetime.today())
        footer.save()
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
