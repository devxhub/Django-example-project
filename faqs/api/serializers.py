from rest_framework import serializers
from faqs.models import *


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class FaqSerializer(serializers.ModelSerializer):

    class Meta:
        model = Faq
        fields = ['id', 'question', 'answer',  'language']
