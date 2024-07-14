from django.shortcuts import render
from cruds.models import detail

def home(request):
    ob = detail.objects.all()
    print(ob)
    return render(request, 'home.html')