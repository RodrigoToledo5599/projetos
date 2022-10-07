from django.urls import path
from .views import *


urlpatterns = [
    path('',TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('create-task/',TaskCreate.as_view(),name='task_form'),
    path('update-task/<int:pk>/',TaskUpdate.as_view(),name='task_update'),
    path('delete-task/<int:pk>/',DeleteView.as_view(),name='task_delete')
]