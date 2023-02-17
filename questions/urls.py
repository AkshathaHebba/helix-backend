from django.urls import include, re_path
from questions import views

urlpatterns = [
    re_path(r'^api/questions', views.questions_list)
]