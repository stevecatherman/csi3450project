from django.shortcuts import render
from django.http import HttpResponse

from project.models import Employee
from project.models import Paycheck
from project.models import Timecard
from project.models import Vacation

from project.forms import Timeform
from project.forms import Vacationform




# Create your views here.

# def index(request):
#    return HttpResponse('Hello, welcome to the index page.')

# Main index page
def home(request):
    return render(request, 'project/home.html')

# Select single employee
#def employee_view(request):
#    obj = Employee.objects.get(employeeid = 2)
#    context = {
#        'first' : obj.fname,
#        'last' : obj.lname,
#   }
#    return render(request, 'project/employee.html', context)

# List all employees from Employee table
def employee_view(request):
    query_set = Employee.objects.all() # raw('SELECT * FROM employee...') is another option - uses cursor object from SQL
    context = {
        'object_instance' : query_set,
    }
    return render(request, 'project/employee.html', context)

# Search for employees in Employee table, by employeeid
def user_employee_query_view(request):
    return render(request, 'project/userEmployeeQuery.html')

# Returns list of employees from search
def user_query_response_view(request):
    minNum = request.GET['minnum']
    maxNum = request.GET['maxnum']
    # Create filtered list
    query_set_employee_id_filtered = []
    # Run the query: extract all results
    query_set_employee_id = Employee.objects.all()
    for object in query_set_employee_id:
        if (object.employeeid >= float(minNum) and object.employeeid <= float(maxNum)):
            query_set_employee_id_filtered.append(object)
    
    context = {
        'object_instance' : query_set_employee_id_filtered
    }
    return render(request, 'project/userQueryResponse.html', context)

# Enter timecard hours
def time_form_view(request):
  if request.method == "POST":
    form = Timeform(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = Timeform()
  return render(request, 'project/timeform.html', {'form': form})


# Search for timecards in Timecard table, by timecardid
def user_employee_timesearch_view(request):
    return render(request, 'project/timesearch.html')

# Return list of timecards from search
def user_timequery_response_view(request):
    minNum = request.GET['minnum']
    maxNum = request.GET['maxnum']
    # Create filtered list
    query_set_timecard_id_filtered = []
    # Run the query: extract all results
    query_set_timecard_id = Timecard.objects.all()
    for object in query_set_timecard_id:
        if (object.timecardid >= float(minNum) and object.timecardid <= float(maxNum)):
            query_set_timecard_id_filtered.append(object)
    
    context = {
        'object_instance' : query_set_timecard_id_filtered
    }
    return render(request, 'project/timecard.html', context)


# Search for paychecks from Paycheck Table, by paycheckid
def user_employee_paysearch_view(request):
    return render(request, 'project/paysearch.html')

# Return list of paychecks from search
def user_payquery_response_view(request):
    minNum = request.GET['minnum']
    maxNum = request.GET['maxnum']
    # Create filtered list
    query_set_paycheck_id_filtered = []
    # Run the query: extract all results
    query_set_paycheck_id = Paycheck.objects.all()
    for object in query_set_paycheck_id:
        if (object.paycheckid >= float(minNum) and object.paycheckid <= float(maxNum)):
            query_set_paycheck_id_filtered.append(object) 

    context = {
        'object_instance' : query_set_paycheck_id_filtered
    }

    return render(request, 'project/paycheck.html', context)

# Enter vacation requests
def vacation_form_view(request):
  if request.method == "POST":
    form = Vacationform(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = Vacationform()
  return render(request, 'project/vacationform.html', {'form': form})

# Search for vacation requests from Vacation Table, by vacationid
def vacation_search_view(request):
    return render(request, 'project/vacationsearch.html')

# Return list of vacation requests from search
def vacation_response_view(request):
    minNum = request.GET['minnum']
    maxNum = request.GET['maxnum']
    # Create filtered list
    query_set_vacation_id_filtered = []
    # Run the query: extract all results
    query_set_vacation_id = Vacation.objects.all()
    for object in query_set_vacation_id:
        if (object.vacationid >= float(minNum) and object.vacationid <= float(maxNum)):
            query_set_vacation_id_filtered.append(object) 

    context = {
        'object_instance' : query_set_vacation_id_filtered
    }

    return render(request, 'project/vacation.html', context)
