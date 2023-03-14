from rest_framework.routers import DefaultRouter
from blogs.api.views import *


router = DefaultRouter()
router.register('posts', PostModelViewSet, basename='posts')
router.register('categories', CategoryModelViewSet, basename='categories')
router.register('tags', TagModelViewSet, basename='tags')
router.register('comments', CommentModelViewSet, basename='comments')
router.register('replies', ReplyModelViewSet, basename='replies')
urlpatterns = router.urls
