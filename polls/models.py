from django.db import models

CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_code = models.IntegerField()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_value = models.IntegerField(choices=CHOICES, default=1)
    choice_code = models.IntegerField(default=0)

class CsvData(models.Model):
    csv_category = models.CharField(max_length=255)
    csv_question = models.CharField(max_length=255)
    csv_code = models.IntegerField()

class CsvSubject(models.Model):
    csv_series = models.CharField(max_length=255)
    csv_subject = models.CharField(max_length=512)
    csv_career = models.CharField(max_length=255)