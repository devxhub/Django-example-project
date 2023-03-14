from rest_framework.routers import DefaultRouter
from jobs.api.views import *


router = DefaultRouter()
router.register('job-circulars', JobCircularModelViewSet,
                basename='job-circulars')
router.register('job-applications', JobApplicationModelViewSet,
                basename='job-applications')
router.register('job-application-statuses',
                JobApplicationStatusModelViewSet, basename='job-application-statuses')

urlpatterns = router.urls
