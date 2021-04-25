from django import forms
from project.models import Timecard
from project.models import Payperiod
from project.models import Employee
from project.models import Jobtype
from project.models import Vacation

# This whole file is part of the updating the database experiment

class Timeform(forms.ModelForm):
  class Meta:
    model = Timecard
    fields = ["jobid", "empid", "payid", "hours",]
    labels = {'jobid' : "Job Type", 'empid' : "Employee ID", 'payid' : "Pay Period", 'hours' : "Hours Worked",}

class Vacationform(forms.ModelForm):
  class Meta:
    model = Vacation
    fields = ["date", "days", "empid", "jobid",]
    labels = {'date' : "Start Date", 'days' : "Number of days", 'empid' : "Employee ID", 'jobid' : "Jobtype ID",}

