from django.urls import path
from . import views

urlpatterns = [
    path('api/simple/employees/<str:pk>', views.employeeListView, name='employeeListView'),
    path('api/apiview/employees/<str:pk>', views.employeeListAPIView, name='employeeListAPIView')
]