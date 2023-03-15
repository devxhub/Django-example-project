from rest_framework.routers import DefaultRouter
from hrm.api.views import *


router = DefaultRouter()

router.register('employees', EmployeeViewSet, basename='employees')
router.register('attendances', AttendanceViewSet, basename='attendances')
router.register('departments', DepartmentViewSet, basename='departments')
router.register('leaves', LeaveViewSet, basename='leaves')

urlpatterns = router.urls
