import itertools
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.db import models
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice, CsvData

class PollView(View):
    template_name = 'index.html'

    def get(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, self.template_name, {'question': question, 'question_id': question_id})

    def post(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)

        # Check if a choice is selected
        choice_value = request.POST.get(f'question_{question_id}')
        choice_code = request.POST.get(f'choice_code_{question_id}')

        if choice_value is not None:
            # Check if there is an existing choice for the current question
            existing_choice = Choice.objects.filter(question=question).first()

            if existing_choice:
                # Update the existing choice
                existing_choice.choice_value = choice_value
                
                # Update choice_code based on the original question's question_code
                existing_choice.choice_code = question.question_code
                
                existing_choice.save()
            else:
                # Save the choice to the database
                choice = Choice.objects.create(
                    question=question,
                    choice_value=choice_value,
                    choice_code=question.question_code  # Set choice_code based on original question
                )

        # Determine the next question ID
        total_questions = Question.objects.count()
        next_question_id = min(total_questions, int(question_id) + 1)

        if next_question_id < total_questions:
            # If there are more questions, go to the next question
            return HttpResponseRedirect(reverse('polls:poll', args=[next_question_id]))
        else:
            # If all questions are completed, redirect to the submission page
            return HttpResponseRedirect(reverse('polls:submit_answers'))

        return render(request, self.template_name, {'question': question, 'question_id': question_id})


class ResultView(View):
    template_name = 'result.html'

    def get(self, request):
        # Get the aggregated data from the Choice model
        aggregated_data = Choice.objects.values('choice_code').annotate(total_value=models.Sum('choice_value'))

        # Create a list of tuples (choice_code, total_value) from aggregated_data
        result_list = [(entry['choice_code'], entry['total_value']) for entry in aggregated_data]

        # Apply quicksort based on the 'total_value'
        sorted_result = self.quicksort(result_list, key=lambda x: x[1])

        # Read CsvData model to get csv_code and csv_category
        csv_data = CsvData.objects.values('csv_code', 'csv_category')

        # Create a dictionary {csv_code: csv_category}
        csv_dict = {entry['csv_code']: entry['csv_category'] for entry in csv_data}

        # Create the final dictionary with three values (choice_code, total_value, csv_category)
        result_dict = {choice_code: {'total_value': total_value, 'csv_category': csv_dict.get(choice_code, None)} for choice_code, total_value in sorted_result}

        # Extract top 3 {key: value} pairs with the highest total_value
        top_3_result = dict(list(result_dict.items())[:3])

        context = {
            'top_3_result': top_3_result,
            'aggregated_data': aggregated_data,
        }

        return render(request, self.template_name, context)

    def quicksort(self, arr, key):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if key(x) > key(pivot)]
        middle = [x for x in arr if key(x) == key(pivot)]
        right = [x for x in arr if key(x) < key(pivot)]
        return self.quicksort(left, key) + middle + self.quicksort(right, key)
