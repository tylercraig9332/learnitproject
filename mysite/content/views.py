from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Lesson
from .models import Word

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
    words = Word.objects.all()
    return render(request, 'learn/listView.html', {'words' : words})
