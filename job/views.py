from django.shortcuts import render
from .models import job
from django.template import Context

# Create your views here.

def job_list(request):
    all_jobs_list = job.objects.all()
    context = {'all_job' : all_jobs_list}
    return render(request,'job/job_list.html',context)


def job_detail(request, id):
    job_detail = job.objects.get(id=id)
    context = {'job' : job_detail}
    return render(request,'job/job_detail.html',context)


