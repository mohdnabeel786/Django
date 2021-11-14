from django import forms
from django.shortcuts import render, HttpResponseRedirect
from .models import Post
from .forms import SignUpForm, LoginForm, DetailsRegistration
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Home
def home(request):
    return render(request, 'chat_box/home.html')

#Dashboard
def user_dashboard(request):
    return render(request, 'chat_box/dashboard.html')


# Signup
def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulation!! Create account Successfully.')
            form.save()
    else:
        form = SignUpForm()
    return render(request, 'chat_box/signup.html', {'form':form})

# Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password =upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully !!')
                    return HttpResponseRedirect('/')
        else:
            form = LoginForm()
        return render(request, 'chat_box/login.html', {'form':form})
    else:
        return HttpResponseRedirect('/')

# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def add_show(request):
    if request.method == 'POST':
        fm = DetailsRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            adds = fm.cleaned_data['address']
            reg = Post(name=nm, email=em, password=pw, address=adds)
            reg.save()
            fm = DetailsRegistration()
    else:
        fm = DetailsRegistration()
    stud = Post.objects.all()
    return render(request, 'chat_box/dashboard.html', {'form':fm, 'stu':stud})

def updateData(request, id):
    if request.method == 'POST':
        pi = Post.objects.get(pk=id)
        fm = DetailsRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Post.objects.get(pk=id)
        fm = DetailsRegistration(instance=pi)
    return render(request, 'chat_box/updateuser.html', {'form':fm})


def deleteData(request, id):
    if request.method == 'POST':
        pi = Post.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')