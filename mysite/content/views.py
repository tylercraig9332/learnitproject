from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Lesson
from .models import Word, WordList
from .forms import AddWordForm, NewWordList

# Create your views here.

def index(request):
    return render(request, 'learn/index.html')

def learn(request):
    lessons = {'lessons': Lesson.objects.all()}
    return render(request, 'learn/learn.html', lessons)


def lesson(request, lesson_id):
    try:
        lesson = Lesson.objects.get(pk=lesson_id)
    except Lesson.DoesNotExist:
        # TODO: Create a template to help handle this.
        raise Http404("Lesson does not exist :(")

    return render(request, 'learn/lessonView.html', {'lesson' : lesson})

def word_list(request):
    if not request.user.is_authenticated:
        return render(request, 'plslogin.html')

    model = WordList()
    user_fields = ['list_name', 'description']
    field_names = ['List Name', "Description"]
    try:
        word_lists = WordList.objects.all()
    except WordList.DoesNotExist:
            raise Http404("We've encountered an error")
    return render(request, 'learn/listView.html', {'lists' : word_lists, 'fields' : user_fields, 'model' : model })

#needs to be fixed to play to the new model-skeem
def list_add(request):
    if not request.user.is_authenticated:
        return render(request, 'plslogin.html')

    if request.method == 'POST':
        form = NewWordList(request.POST)
    else:
        raise Http404("We've encountered an error - See line 50 in content/views.py")
    return render(request, 'learn/listAddView.html',  {'listData' : form})

def list_view(request):
    if not request.user.is_authenticated:
        return render(request, 'plslogin.html')

    # TODO: add a view that takes in form data from listAddView and puts in
    # in the database and renders a page that views the list.

def pls_login(request):
    if request.user.is_authenticated:
        return render(request, '/')

    return render(request, 'learn/plslogin.html')
