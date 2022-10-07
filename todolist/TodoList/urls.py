from django.urls import path
from .views import *


urlpatterns = [
    path('',TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('create-task/',TaskCreate.as_view(),name='task_form'),
    
    path('delete-task/<int:pk>/',DeleteView.as_view(),name='task_delete')
]