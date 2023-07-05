from django.urls import path
from main.views import *

urlpatterns = [
    path('<int:pk>/', DetailTask.as_view()),
    path('', ListTask.as_view()),
    path('create', CreateTask.as_view()),
    path('delete/<int:pk>', DeleteTask.as_view())
]
