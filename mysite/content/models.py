from django.db import models


class Lesson(models.Model):
    title = models.CharField(max_length=50)
    pdf_start = models.IntegerField()
    pdf_end = models.IntegerField()
    is_review = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Word(models.Model):
    word = models.CharField(max_length=50, help_text="Word")
    translation = models.CharField(max_length=50, help_text="Translation")

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
