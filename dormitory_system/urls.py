"""dormitory_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from dormitory import views

urlpatterns = [
    url(r'^student_login/', views.student_login, name='student_login'),
    url(r'^get_question/', views.get_question, name='get_question'),
    url(r'^save_answer/', views.save_answer, name='save_answer'),
    url(r'^get_result/', views.get_result, name='get_result'),
    url(r'^admin_login/', views.admin_login, name='admin_login'),
    url(r'^percentage/', views.percentage, name='percentage'),
    url(r'^output_all/', views.output_all, name='output_all'),
    url(r'^admin/', admin.site.urls),
]
