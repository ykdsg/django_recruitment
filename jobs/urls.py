from django.conf.urls import url

from jobs import views

urlpatterns=[
    url(r"^joblist/",views.joblsit,name = "jobList")
]