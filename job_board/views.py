from django.shortcuts import render,HttpResponse, get_object_or_404
from .models import JobPosting
# Create your views here.
def index(request):
    active_jobs = JobPosting.objects.filter(is_active=True)
    context = {
        'active_jobs': active_jobs
    }

    return render(request, 'job_board/index.html', context)
def job_detail(request, job_id):
    job = get_object_or_404(JobPosting, id= job_id)
    context = {
        'job': job
    }
    return render(request, 'job_board/job_detail.html', context)