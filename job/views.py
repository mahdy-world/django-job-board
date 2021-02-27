from django.shortcuts import render , redirect
from .models import *
from django.template import Context
from django.core.paginator import Paginator
from .form import ApplyForm ,JobForm
from django.urls import reverse

# Create your views here.

def job_list(request):
    all_jobs_list = job.objects.all()

    paginator = Paginator(all_jobs_list, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'all_job' : page_obj}

    return render(request,'job/job_list.html',context)


def job_detail(request, slug):
    job_detail = job.objects.get(slug=slug)

    if request.method=='POST':
        form = ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)  
            myform.job =  job_detail
            myform.save()  
            return redirect(reverse())   

    else:
        form = ApplyForm()         

    context = {'job' : job_detail , 'form' : ApplyForm}
    return render(request,'job/job_detail.html',context)


def add_job(request):

    if request.method=='POST':
        form = JobForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save() 
            return redirect(reverse('jobs:job_list'))
    else:
        form = JobForm()    
    
    return render(request,'job/add_job.html',{'form':form})


