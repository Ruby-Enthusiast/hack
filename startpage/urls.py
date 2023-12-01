from django.urls import path
from .views import start_page, start_page_view, second_page, show_links

app_name = 'startpage'
urlpatterns = [
    path('start_page/', start_page, name='start_page'),
    path('start_page_view/', start_page_view, name='start_page_view'),
    path('second/', second_page, name='second_page'),
    path('show_links/', show_links, name='show_links'),
]