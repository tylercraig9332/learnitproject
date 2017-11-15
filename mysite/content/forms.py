from .models import Word, WordList
from django import forms
from django.forms import ModelForm


class AddWordForm(forms.Form):
    list_name = forms.CharField(label="List Name", max_length=40)

class WordListForm(ModelForm):
    class Meta:
        model = WordList
        fields = ['title', 'description', 'words', 'author']
