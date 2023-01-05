from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

from .forms import PersonForm
from django.http import JsonResponse
import json
from .models import BranchModel, DetailsModel


def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.set_password(password)
                user.save()
                return redirect('/login')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('/register')
    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/add_person')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('/login')
    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def person(request):
    form = PersonForm()
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "person.html", {"form": form})


def branches(request):
    data = json.loads(request.body)
    branches = BranchModel.objects.filter(district__id=data['user_id'])
    print(branches)
    return JsonResponse(list(branches.values("id", "name")), safe=False)


def details(request):
    d = DetailsModel.objects.all()
    if request.method == 'POST':
        Name = request.POST.get('Name', '')
        Contact_Number = request.POST.get('Contact_Number', )

        task = DetailsModel(Name=Name, Contact_Number=Contact_Number)
        task.save()

    return render(request, 'details.html', {'d': d})
