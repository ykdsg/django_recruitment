from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status, mixins, generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer



# ------------------------------snippet--------------------------

# class SnippetList(APIView):
#     """
#     列出所有的snippets或者创建一个新的snippet。
#     """
#     def get(self, request, format=None):
#         sinppet = Snippet.objects.all()
#         serializer= SnippetSerializer(sinppet,many=True)
#         return Response(serializer.data)
#
#
#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# class SnippetDetail(APIView):
#     """
#     检索，更新或删除一个snippet示例。
#     """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# 使用混合mixins，可以轻松复用
# 使用GenericAPIView构建了我们的视图，
# 并且用上了ListModelMixin和CreateModelMixin。 基类提供核心功能，而mixin类提供.list()和.create()操作。
# 然后我们明确地将get和post方法绑定到适当的操作。
# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     # 修改实例保存的方法，并处理传入请求或请求URL中隐含的任何信息。
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     # IsOwnerOrReadOnly 是自定义的权限控制器
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# 可以使用通用基类，不过感觉这个有点过于简化了
# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer


# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     renderer_classes = (renderers.StaticHTMLRenderer,)
#
#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)



class SnippetViewSet(viewsets.ModelViewSet):
    """
        此视图自动提供`list`，`create`，`retrieve`，`update`和`destroy`操作。

        另外我们还提供了一个额外的`highlight`操作。
        """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    # 使用@action 装饰器创建一个名为highlight的自定义操作。这个装饰器可用于添加不符合标准create/update/delete样式的任何自定义路径。
    # 默认情况下，使用@action 装饰器的自定义操作将响应GET请求。如果我们想要一个响应POST请求的动作，我们可以使用methods参数。
    @action(detail=True,renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# ----------------------------user ------------------------------------

# 将用户展示为只读视图，因此我们将使用ListAPIView和RetrieveAPIView通用的基于类的视图。
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# ViewSet类与View类几乎相同，不同之处在于它们提供诸如read或update之类的操作，而不是get或put等方法处理程序。
# 最后一个ViewSet类只绑定到一组方法处理程序，当它被实例化成一组视图的时候，通常通过使用一个Router类来处理自己定义URL conf的复杂性。

# 将UserList和UserDetail视图重构为一个UserViewSet。我们可以删除这两个视图，并用一个类替换它们：
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    此视图自动提供`list`和`detail`操作。
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer





@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # 使用REST框架的reverse功能来返回完全限定的URL
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })
