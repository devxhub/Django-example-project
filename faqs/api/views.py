from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from faqs.models import *
from faqs.api.serializers import *


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class FaqView(viewsets.ModelViewSet):
    queryset = Faq.objects.all().prefetch_related('language').all()
    serializer_class = FaqSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['language']
