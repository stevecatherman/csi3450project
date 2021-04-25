from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
#    path('', views.index, name='index'), # localhost:8000
#    path('login/', LoginView.as_view(template_name='project/userLogin.html'), name="Login"),
    path('', LoginView.as_view(template_name='project/userLogin.html'), name="Login"),
    path('home', views.home, name='home'),
    path('employee/', views.employee_view, name='employee'),
    path('useremployeequery', views.user_employee_query_view, name='useremployeequery'),
    path('userqueryresponse', views.user_query_response_view, name='userqueryresponse'),
    path('timeform', views.time_form_view, name='timeform'), 
    path('timesearch', views.user_employee_timesearch_view, name='timesearch'),
    path('timecard', views.user_timequery_response_view, name='timecard'),    
    path('paysearch', views.user_employee_paysearch_view, name='paysearch'),
    path('paycheck', views.user_payquery_response_view, name='paycheck'), 
    path('vacationform', views.vacation_form_view, name='vacationform'),
    path('vacationsearch', views.vacation_search_view, name='vacationsearch'),
    path('vacation', views.vacation_response_view, name='vacation'),  
] 