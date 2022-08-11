from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views_0, views

urlpatterns = [
    url(r'^snippets/$',views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),

    # url(r'^snippets/$', views.snippet_list),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]

# 可以为API路径添加对格式后缀的支持。使用格式后缀给我们明确指定了给定格式的URL，
# 这意味着我们的API将能够处理诸如http://127.0.0.1:8000/snip/snippets/1.json 之类的URL。
urlpatterns=format_suffix_patterns(urlpatterns)