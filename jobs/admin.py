from django.contrib import admin
from .models import *


class JobCircularAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'vacancy', 'is_published',
                    'experience', 'salary', 'deadline',)
    list_filter = ('type', 'created_at',)
    search_fields = ('title', 'type', 'location',)
    list_editable = ('is_published',)
    list_per_page = 10


class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('circular', 'name',  'created_at',)
    list_filter = ('created_at',)
    list_per_page = 10


class JobApplicationStatusAdmin(admin.ModelAdmin):
    list_display = ('application', 'status', )
    list_filter = ('status',)
    search_fields = ('status', 'application_name')
    list_per_page = 10


admin.site.register(JobCircular, JobCircularAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
admin.site.register(JobApplicationStatus, JobApplicationStatusAdmin)
