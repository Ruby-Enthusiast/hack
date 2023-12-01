# urls.py

from django.urls import path
from .views import PollView, ResultView

app_name = 'polls'

urlpatterns = [
    path('<int:question_id>/', PollView.as_view(), name='poll'),
    path('submit_answers/', ResultView.as_view(), name='submit_answers'),
]