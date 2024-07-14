from django.shortcuts import render
from cruds.models import detail

def home(request):
    data = request.POST
    if request.method == 'POST':
        name = data.get('name')
        email_id = data.get('email')
        branch = data.get('branch')
        section = data.get('section')
        year = data.get('year')
        dob = data.get('dob')
        ob = detail(name=name, email_id=email_id, branch=branch, section=section, year=year, dob=dob)
        ob.save()
    return render(request, 'home.html')


def detail_page(request):
    ob = detail.objects.all()
    if ob:
        x=[]
        for i in ob:
            x.append(i)
    return render(request, 'detail_page.html', {'key':x})