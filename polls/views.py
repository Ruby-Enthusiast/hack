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

        # Create a dictionary {choice_code: total_value} directly from aggregated_data
        result_dict = {entry['choice_code']: entry['total_value'] for entry in aggregated_data}

        context = {
            'result_dict': result_dict,
            'aggregated_data': aggregated_data,
        }

        return render(request, self.template_name, context)

