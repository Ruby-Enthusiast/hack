# comments/urls.py
from django.urls import path
from .views import comments_list_and_add, delete_comment

urlpatterns = [
    path('<code>/comments/', comments_list_and_add, name='comments_list_and_add'),
    path('<code>/comments/delete/<int:comment_id>/', delete_comment, name='delete_comment'),
]
