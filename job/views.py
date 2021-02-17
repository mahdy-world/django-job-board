from django.shortcuts import render
from .models import job
from django.template import Context
from django.core.paginator import Paginator

# Create your views here.

def job_list(request):
    all_jobs_list = job.objects.all()

    paginator = Paginator(all_jobs_list, 1) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'all_job' : page_obj}

    return render(request,'job/job_list.html',context)


def job_detail(request, id):
    job_detail = job.objects.get(id=id)
    context = {'job' : job_detail}
    return render(request,'job/job_detail.html',context)


