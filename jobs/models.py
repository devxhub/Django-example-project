from django.db import models
from django_quill.fields import QuillField
from django.utils.translation import gettext_lazy as _
from .choices import *
from django.core.exceptions import ValidationError


def validate_file_extension(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError('Only PDF files are allowed.')


class JobCircular(models.Model):
    title = models.CharField(max_length=155)
    type = models.CharField(max_length=100, choices=JOB_TYPE)
    location = models.CharField(max_length=255)
    vacancy = models.IntegerField()
    image = models.ImageField(upload_to='images/job_circulars/')
    description = QuillField()
    experience = models.CharField(max_length=100)
    age_range = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GENDER)
    salary = models.CharField(max_length=100)
    working_hour = models.CharField(max_length=100)
    deadline = models.DateTimeField()
    is_published = models.BooleanField(default=False)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    name = models.CharField(max_length=155)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    circular = models.ForeignKey(JobCircular, on_delete=models.CASCADE)
    cv = models.FileField(
        upload_to='files/cv/', verbose_name=_('Candidate CV'), validators=[validate_file_extension])
    cover_letter = models.FileField(upload_to='files/cover_letter/', verbose_name=_(
        'Candidate Cover Letter'), validators=[validate_file_extension])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class JobApplicationStatus(models.Model):
    application = models.ForeignKey(JobApplication, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=APPLICATION_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.application.name
