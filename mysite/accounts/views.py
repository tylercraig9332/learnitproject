from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


# Create your views here.
def profile(request):
    userdata = request.user
    return render(request, 'accounts/profile.html', {'user' : userdata})

def inbox(request):
    return render(request, 'accounts/inbox.html')

def account_edit(request):
    userdata = request.username
    return render(request, 'accounts/account_edit.html', {'user' : userdata})
