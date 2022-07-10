from django.urls import path
from . import views

urlpatterns = [
    path('api/employees/<str:pk>', views.employeeListView, name='employeeListView')
]