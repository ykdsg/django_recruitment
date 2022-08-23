"""django_recruitment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
# from jobs import views

import quickstart.views

router = routers.DefaultRouter()
router.register(r'users', quickstart.views.UserViewSet)
router.register(r'groups', quickstart.views.GroupViewSet)

urlpatterns = [
    url(r"job/",include('jobs.urls')),
    url(r"^snip/",include('snippets.urls')),
    # 使用的是viewsets而不是views，所以可以通过简单地使用路由器类注册视图来自动生成API的URL conf。
    url(r"^",include(router.urls)),



    path('admin/', admin.site.urls),
    path('book/api/',include('books.urls'))
]
