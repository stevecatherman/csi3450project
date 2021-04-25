from django.contrib import admin
from project.models import Employee
from project.models import Jobtype
from project.models import Paycheck
from project.models import Timecard
from project.models import Vacation
from project.models import Payperiod

# Register your models here.
admin.site.register(Employee)
admin.site.register(Jobtype)
admin.site.register(Paycheck)
admin.site.register(Timecard)
admin.site.register(Vacation)
admin.site.register(Payperiod)
