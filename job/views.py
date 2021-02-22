from django.shortcuts import render
from .models import job
from django.template import Context
from django.core.paginator import Paginator
from .form import ApplyForm

# Create your views here.

def job_list(request):
    all_jobs_list = job.objects.all()

    paginator = Paginator(all_jobs_list, 1) # Show 25 contacts per page.

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

    else:
        form = ApplyForm()         

    context = {'job' : job_detail , 'form' : ApplyForm}
    return render(request,'job/job_detail.html',context)


