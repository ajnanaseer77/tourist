from django.shortcuts import render
from . models import destination
from . models import placenew

# Create your views here.
def fun(request):
    obj = destination.objects.all()
    obj1 = placenew.objects.all()
    return render(request, 'index.html',{'results':obj,'new':obj1})

def addition(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    num3 = num1 + num2
    return render(request, 'result.html', {'add': num3})