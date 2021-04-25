from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # localhost:8000/admin
    path('', include('project.urls'))
]
