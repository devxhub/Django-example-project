from django.contrib import admin
from hrm.models import *


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'mobile', 'email',)
    search_fields = ('first_name', 'last_name', 'email', 'mobile',)
    list_filter = ('department',)
    list_per_page = 20


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('staff', 'date', 'first_in', 'last_out', 'status',)
    search_fields = ('staff__first_name', 'staff__last_name',
                     'staff__email', 'staff__mobile',)
    list_filter = ('status',)
    list_per_page = 20


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_per_page = 20


class LeaveAdmin(admin.ModelAdmin):
    list_display = ('employee', 'start', 'end', 'status',)
    search_fields = ('employee__first_name', 'employee__last_name',
                     'employee__email', 'employee__mobile',)
    list_filter = ('status',)
    list_per_page = 20


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Leave, LeaveAdmin)
