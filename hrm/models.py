from django.db import models
import random
from django.utils import timezone
import datetime


class Department(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    history = models.TextField(
        max_length=1000, null=True, blank=True, default='No History')

    def __str__(self):
        return self.name


class Employee(models.Model):
    LANGUAGE = (('english', 'ENGLISH'), ('bangla', 'BANGLA'),
                ('hindi', 'HINDI'), ('french', 'FRENCH'))
    GENDER = (('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER'))
    emp_id = models.CharField(
        max_length=70, default='emp'+str(random.randrange(100, 999, 1)))
    thumb = models.ImageField(blank=True, null=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=125, null=False)
    address = models.TextField(max_length=100, default='')
    emergency = models.CharField(max_length=11)
    gender = models.CharField(choices=GENDER, max_length=10)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True)
    joined = models.DateTimeField(default=timezone.now)
    language = models.CharField(
        choices=LANGUAGE, max_length=10, default='english')
    nuban = models.CharField(max_length=10, default='0123456789')
    bank = models.CharField(max_length=25, default='First Bank Ltd.')
    salary = models.CharField(max_length=16, default='00,000.00')

    def __str__(self):
        return self.first_name


class Attendance (models.Model):
    STATUS = (('PRESENT', 'PRESENT'), ('ABSENT', 'ABSENT'),
              ('UNAVAILABLE', 'UNAVAILABLE'))
    date = models.DateField(auto_now_add=True)
    first_in = models.TimeField(null=True, default=datetime.time(0, 0, 0))
    last_out = models.TimeField(null=True, default=datetime.time(0, 0, 0))
    status = models.CharField(choices=STATUS, max_length=15)
    staff = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return 'Attendance -> '+str(self.date) + ' -> ' + str(self.staff)


class Leave (models.Model):
    STATUS = (('approved', 'APPROVED'), ('unapproved',
              'UNAPPROVED'), ('decline', 'DECLINED'))
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    start = models.CharField(blank=False, max_length=15)
    end = models.CharField(blank=False, max_length=15)
    status = models.CharField(
        choices=STATUS,  default='Not Approved', max_length=15)

    def __str__(self):
        return self.employee + ' ' + self.start
