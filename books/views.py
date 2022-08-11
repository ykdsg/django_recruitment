from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from books.models import Books
from books.serializer import BooksSerializer


# DRF通过视图集ViewSet的方式让我们对某一个数据类Model可以进行增删改查，而且不同的操作对应于不同的请求方式，比如查看所有books用get方法，添加一本book用post方法等，让整个后端服务是restful的。
class BooksViewSet(viewsets.ModelViewSet):
    queryset=Books.objects.all()
    serializer_class = BooksSerializer


