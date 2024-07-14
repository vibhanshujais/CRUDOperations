from django.shortcuts import render
from cruds.models import detail

def home(request):

    return render(request, 'home.html')


def detail_page(request):
    ob = detail.objects.all()
    if ob:
        for i in ob:
            print(i)
    return render(request, 'detail_page.html')