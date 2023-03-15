from hrm.api.serializers import *
from hrm.models import *
from rest_framework import viewsets
from rest_framework import filters


# Create your views here.


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name',
                     'email', 'mobile', 'department__name']


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['staff__first_name', 'staff__last_name',
                     'staff__email', 'staff__mobile', 'status']


class LeaveViewSet(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['employee__first_name', 'employee__last_name',
                     'employee__email', 'employee__mobile', 'status']
