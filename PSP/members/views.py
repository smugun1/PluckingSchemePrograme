from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.

# Signup

def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully!!!')
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'authenticate/signup.html', {'form': fm})


# Login

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully!!!')
                    return render(request, 'authenticate/profile.html')
                    # return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'authenticate/userlogin.html', {'form': fm})
    else:
        return render(request, 'authenticate/profile.html')
        # return HttpResponseRedirect('/profile/')


# Profile
@login_required
def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'authenticate/profile.html', {'name': request.user})
    else:
        return render(request, 'authenticate/userlogin.html')
        # return HttpResponseRedirect('/login/')


# Logout
@login_required
def user_logout(request):
    logout(request)

    return render(request, 'authenticate/userlogout.html', {'name': request.user})

