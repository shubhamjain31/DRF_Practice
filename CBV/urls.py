from django.urls import path
from . import views

urlpatterns = [
    # path('api/simple/employees/<str:pk>', views.employeeListView, name='employeeListView'),
    path('api/apiview/courses', views.CourseListAPIView.as_view(), name='CourseListAPIView.as_view()')
]