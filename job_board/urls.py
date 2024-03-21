
from django.urls import path

from job_board.views import index, job_detail

urlpatterns = [
    path('', index),
    path('job/<int:job_id>/',job_detail, name='job_detail'),
    
]