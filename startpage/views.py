# start_page/views.py
import random
from django.shortcuts import render, redirect
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
    return redirect('startpage:second_page')


def start_page(request):
    return render(request, 'start_page.html')

def second_page(request):
    return render(request, 'second_page.html')

from polls.models import CsvData
from django.shortcuts import render

def show_links(request):
    # Fetch data from CsvData model
    csv_data = CsvData.objects.filter(csv_code__range=(101, 116)).values('csv_code', 'csv_category')

    # Create a dictionary with key as range(101, 117) and value as csv_category
    links_dict = {entry['csv_code']: entry['csv_category'] for entry in csv_data}

    # Pass the dictionary to the template
    context = {'links_dict': links_dict}
    return render(request, 'show_links.html', context)