from rest_framework import serializers
from django_quill.fields import QuillField
from jobs .models import *


class JobCircularSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField(
        method_name='get_description')

    def get_description(self, obj):
        return obj.description.html if obj.description else None

    class Meta:
        model = JobCircular
        fields = '__all__'


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'


class JobApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplicationStatus
        fields = '__all__'
