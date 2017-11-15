from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


# Create your views here.
def profile(request):
    userdata = request.user.get_profile()
    return(request, 'accounts/profile.html', {'user' : userdata})
