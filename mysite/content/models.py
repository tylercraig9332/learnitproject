from django.db import models


class Lesson(models.Model):
    title = models.CharField(max_length=50)
    pdf_start = models.IntegerField()
    pdf_end = models.IntegerField()
    is_review = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Word(models.Model):
    word_id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=50, help_text="Word")
    translation = models.CharField(max_length=50, help_text="Translation in Target Language")

    NOUN = 'N'
    VERB = 'V'
    ADJ = 'ADJ'
    OTHER = 'OTR'
    WORD_TYPES = (
        (NOUN, 'Noun'),
        (VERB, 'Verb'),
        (ADJ, 'Adjective'),
        (OTHER, 'Other'))
    word_type = models.CharField(
        max_length=3,
        choices=WORD_TYPES,
        default=NOUN
    )

    def __str__(self):
        return self.word

class WordList(models.Model):
    name = models.CharField(max_length=50, help_text="Name Of List")
    # TODO: need to identify the way Django stores user ids
    user = models.IntegerField()
    date_created = models.DateField(auto_now=True)
    word_ids = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name
