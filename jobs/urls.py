from django.conf.urls import url

from jobs import views

urlpatterns=[
    url(r"^joblist/",views.joblsit,name = "jobList"),
    # job/后面的参数是一个数字（\d+），对这个匹配赋值给job_id
    url(r"^job/(?P<job_id>\d+)/$", views.detail, name="detail"),
]