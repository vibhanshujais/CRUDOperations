from django.shortcuts import render
from cruds.models import detail

def home(request):
    ob = detail.objects.all()
    if ob:
        print(ob)

    return render(request, 'home.html')