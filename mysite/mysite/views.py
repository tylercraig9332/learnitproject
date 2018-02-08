from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as lg
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import Http404


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'oldsignup.html', {'form': form})


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        lg(request, user)
        return render(request, 'oldlogin.html', {'user' : user})
    else:
        return Http404("Error occured with loging in user")

def logout(request):
    logout(request)
