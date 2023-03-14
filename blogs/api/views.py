from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework_json_api.pagination import JsonApiLimitOffsetPagination
from blogs.models import *
from .serializers import *


class LimitPagination(JsonApiLimitOffsetPagination):
    offset_query_param = 'offset'
    limit_query_param = 'limit'
    default_limit = 5
    max_limit = None


class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(is_published=True).order_by('-created_at')
    serializer_class = PostListModelSeriliazer
    pagination_class = LimitPagination
    http_method_names = ['get']
    detail_serializer_class = PostDetailModelSeriliazer
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            if hasattr(self, 'detail_serializer_class'):
                return self.detail_serializer_class

        return super(PostModelViewSet, self).get_serializer_class()


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSeriliazer
    pagination_class = PageNumberPagination
    http_method_names = ['get']


class TagModelViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagModelSeriliazer
    pagination_class = PageNumberPagination
    http_method_names = ['get']


class CommentModelViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentModelSeriliazer
    pagination_class = PageNumberPagination
    http_method_names = ['get']


class ReplyModelViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplyModelSeriliazer
    pagination_class = PageNumberPagination
    http_method_names = ['get']
