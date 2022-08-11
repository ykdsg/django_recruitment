from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from django.template import loader

from jobs.models import Job, Cities, JobTypes


# 在视图层把页面加进来
def joblsit(request):
    # 通过数据库加载
    job_list=Job.objects.order_by('job_type')
    template = loader.get_template('joblist.html')
    context ={'job_list':job_list}

    # 转换一下int类型为string类型
    for job in job_list:
        job.city_name = Cities[job.job_city][1]
        job.job_type = JobTypes[job.job_type][1]

    return HttpResponse(template.render(context))


def detail(request,job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.city_name = Cities[job.job_city][1]
    except Job.DoesNotExist:
        raise Http404("Job dose not exist")

    return render(request,'job.html',{'job':job})

