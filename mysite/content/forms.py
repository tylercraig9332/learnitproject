from .models import Word, WordList
from django import forms
from django.forms import ModelForm


class NewWordList(forms.Form):
    list_name = forms.CharField(label="newList", max_length=50)


class AddWordForm(forms.Form):
    list_name = forms.CharField(label="List Name", max_length=40)
'''
class WordListForm(ModelForm):
    class Meta:
        model = WordList
        fields = ['title', 'description', 'words', 'author']
'''
# Passes data - so I should implement a way to add a new entry to the database
# from the given form.
class WordListForm(forms.Form):
    list_name = forms.CharField(label="List Name", max_length=30)
    #user_data = request.user_id // or something like this
    #date_created = Whatever the current time is.
    #word_ids = null
    #description = null

    #from here to the view model update database and session with the given data associated with the user.
