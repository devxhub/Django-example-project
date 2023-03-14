from rest_framework import serializers
from django.contrib.humanize.templatetags import humanize
from blogs.models import *


class AuthroModelSeriliazer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_name')

    class Meta:
        model = Author
        fields = "__all__"
        include = ['name']

    def get_name(self, obj):
        if obj.user:
            return obj.user.first_name + ' ' + obj.user.last_name
        else:
            return None


class CategoryModelSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagModelSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PostListModelSeriliazer(serializers.HyperlinkedModelSerializer):
    categories = CategoryModelSeriliazer(many=True)
    tags = TagModelSeriliazer(many=True)
    author = AuthroModelSeriliazer(many=False)
    read_time = serializers.SerializerMethodField(method_name='get_read_time')
    created_at = serializers.SerializerMethodField(method_name='get_created_at')
    url = serializers.HyperlinkedIdentityField(
        view_name='posts-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Post
        fields = ["url", 'id', 'title', 'slug', 'image', 'author',
                  'categories', 'tags', 'read_time', 'created_at',]

    def get_read_time(self, obj):
        return obj.get_read_time()

    def get_created_at(self, obj):
        return humanize.naturaltime(obj.created_at)


class PostDetailModelSeriliazer(serializers.ModelSerializer):
    categories = CategoryModelSeriliazer(many=True)
    tags = TagModelSeriliazer(many=True)
    author = AuthroModelSeriliazer(many=False)
    read_time = serializers.SerializerMethodField(method_name='get_read_time')
    content = serializers.SerializerMethodField(method_name='get_content')
    comment = serializers.SerializerMethodField(method_name='get_comment')

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'image', 'author',
                  'categories', 'tags', 'read_time', "content", "comment" ]

    def get_read_time(self, obj):
        return obj.get_read_time()

    def get_content(self, obj):
        return obj.content.html
    
    def get_comment(self, obj):
        return CommentModelSeriliazer(obj.comment_set.all(), many=True).data
    


class CommentModelSeriliazer(serializers.ModelSerializer):

    reply = serializers.SerializerMethodField(method_name='get_reply')

    class Meta:
        model = Comment
        fields = ['id', 'name', 'email', 'comment', 'created_at', 'reply']

    def get_reply(self, obj):
        return ReplyModelSeriliazer(obj.reply_set.all(), many=True).data

class ReplyModelSeriliazer(serializers.ModelSerializer):
  
    class Meta:
        model = Reply
        exclude = ['comment'] 
