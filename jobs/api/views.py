from rest_framework import viewsets
from jobs.models import *
from . serializers import *


class JobCircularModelViewSet(viewsets.ModelViewSet):
    queryset = JobCircular.objects.all()
    serializer_class = JobCircularSerializer


class JobApplicationModelViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer


class JobApplicationStatusModelViewSet(viewsets.ModelViewSet):
    queryset = JobApplicationStatus.objects.all()
    serializer_class = JobApplicationStatusSerializer
