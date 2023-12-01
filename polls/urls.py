# urls.py

from django.urls import path
from .views import PollView, submit_answers

app_name = 'polls'

urlpatterns = [
    path('<int:question_id>/', PollView.as_view(), name='poll'),
    path('submit_answers/', submit_answers, name='submit_answers'),
]
