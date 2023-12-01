# start_page/views.py
import random
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from polls.models import Question, CsvData

def start_page_view(request):
    # Get 64 random CsvData records
    random_csv_data = random.sample(list(CsvData.objects.all()), 64)

    # Update Question objects with CsvData
    for question, csv_data in zip(Question.objects.all(), random_csv_data):
        question.question_text = csv_data.csv_question
        question.question_code = csv_data.csv_code
        question.save()

    # Redirect to the first question
    return HttpResponseRedirect(reverse('polls:poll', args=[1]))


def start_page(request):
    return render(request, 'start_page.html')