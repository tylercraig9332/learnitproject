from django.db import models

# Create your models here.

class Lesson(models.Model):
    title = models.CharField(max_length=50)
    pdf_start = models.IntegerField()
    pdf_end = models.IntegerField()
    is_review = models.BooleanField(default=False)

class Memeber(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=30)
    current_lesson = models.IntegerField(default=1)
    email = models.CharField(blank=True, max_length=100)


    def __str__(self):
        return self.title
