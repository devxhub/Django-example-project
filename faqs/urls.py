from rest_framework.routers import DefaultRouter
from faqs.api.views import *

router = DefaultRouter()

router.register('languages', LanguageView, basename='languages')
router.register('faqs', FaqView, basename='faqs')

urlpatterns = router.urls

