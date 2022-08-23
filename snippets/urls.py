from django.conf.urls import url
from django.urls import include, path
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views_0, views
from snippets.views import SnippetViewSet, UserViewSet, api_root

# 通过viewset绑定了http方法到具体的action
# 将资源绑定到了具体的视图中
snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

#
router=DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [

    # 基于方法视图
    # url(r'^snippets/$', views.snippet_list),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),

    # 基于类视图
    # url(r'^$', views.api_root),
    # url(r'^snippets/$',views.SnippetList.as_view(),name='snippet-list'),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(),name='snippet-detail'),
    # url(r'^users/$', views.UserList.as_view(),name='user-list'),
    # url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(),name='user-detail'),
    # url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(),name='snippet-highlight'),


    # 注册视图
    # path('', api_root),
    # path('snippets/', snippet_list, name='snippet-list'),
    # path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    # path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    # path('users/', user_list, name='user-list'),
    # path('users/<int:pk>/', user_detail, name='user-detail')

    # 因为我们使用的是ViewSet类而不是View类，我们实际上不需要自己设计URL。将资源连接到视图和url的约定可以使用Router类自动处理。我们需要做的就是使用路由器注册相应的视图集，然后让它执行其余操作。
    # 使用路由器注册viewsets类似于提供urlpattern。我们包含两个参数 - 视图的URL前缀和视图本身。
    # DefaultRouter类也会自动为我们创建API根视图，因此我们现在可以从我们的views模块中删除api_root方法。
    # 但是使用视图集不像单独构建视图那样明确。
    path('', include(router.urls)),

]

# 可以为API路径添加对格式后缀的支持。使用格式后缀给我们明确指定了给定格式的URL，
# 这意味着我们的API将能够处理诸如http://127.0.0.1:8000/snip/snippets/1.json 之类的URL。
# 使用path('', include(router.urls)) 之后，再加上format_suffix_patterns 会报错。
# urlpatterns=format_suffix_patterns(urlpatterns)

urlpatterns += [
    # 添加登录入口
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]