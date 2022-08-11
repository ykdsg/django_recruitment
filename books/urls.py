from django.urls import path, include
from rest_framework.routers import DefaultRouter

from books import views

# 使用viewsets，可以通过简单地使用路由器类注册视图来自动生成API的URL conf
router= DefaultRouter()
router.register('books', views.BooksViewSet)

# 如果我们需要对API URL进行更多的控制，我们可以简单地将其拉出来使用常规基于类的视图，并明确地编写URL conf。

urlpatterns=[
    path('', include(router.urls))
]
