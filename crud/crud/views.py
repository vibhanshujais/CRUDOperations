from django.shortcuts import render, redirect
from cruds.models import detail

def home(request):
    try:
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
    except:
        return redirect('/')


def detail_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email_id = request.POST.get('email')
        branch = request.POST.get('branch')
        year = request.POST.get('year')
        section = request.POST.get('section')
        dob = request.POST.get('dob')
        ob = detail.objects.filter(email_id=email_id)
        ob = ob.update(name=name, branch=branch, section=section, year=year, dob=dob, email_id=email_id)
    ob = detail.objects.all()
    if ob:
        x=[]
        for i in ob:
            x.append(i)
        return render(request, 'detail_page.html', {'key':x})
    return render(request, 'detail_page.html')


def update_record(request,email):
    ob = detail.objects.filter(email_id=email)
    x=[]
    for i in ob:
        x.append(i)
    return render(request, 'update_detail.html', {'key':x})


def delete_record(request, email):
    ob  = detail.objects.filter(email_id = email)
    ob.delete()
    return render(request, 'detail_page')