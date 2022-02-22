from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Login
from datetime import datetime

# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        info = Login(username=username, password=password,contact=contact, address=address, date=datetime.today())
        info.save()
        return HttpResponse('Details is Submitted')
    return render(request, 'login.html')


def data(request):
    if request.method == "POST":
        sear = request.POST.get('sea')
        fm1 = Login.objects.filter(username__contains =sear)
        return render(request, 'data.html', {'ash': fm1})
    else:
        fm = Login.objects.all
        return render(request, 'data.html', {'ash': fm})


def base(request):
    return render(request, 'base.html')


def delete(request,id):
    if request.method == "POST":
        d = Login.objects.get(pk=id)
        d.delete()
        return HttpResponseRedirect('/data/')

def update(request,id):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        info = Login(username=username, password=password,contact=contact, address=address, id=id,date=datetime.today())
        info.save()
        return HttpResponseRedirect('/data/')
    return render(request,'update.html')