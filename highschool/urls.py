"""
URL configuration for highschool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path, re_path
from startpage.views import start_page, start_page_view

def poll_code_view(request, code):
    # Use the code to dynamically construct the template name
    template_name = f'{code}.html'
    return render(request, template_name, {'question_id': code})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("polls/", include('polls.urls')),
    path("startpage/", include('startpage.urls')),
    re_path(r'^(?P<code>\d+)/$', poll_code_view, name='poll_code'),
    re_path(r'^$', start_page, name='root_redirect'),
]
