from django.urls import path
from . import views

urlpatterns = [
    # path('api/simple/employees/<str:pk>', views.employeeListView, name='employeeListView'),
    path('api/apiview/courses/<str:pk>', views.CourseListAPIView.as_view(), name='CourseListAPIView.as_view()'),
    path('api/apiview/courses', views.CourseListAPIView.as_view(), name='CourseListAPIView.as_view()'),

    path('api/mixins/courses', views.CourseListMixin.as_view(), name='CourseListMixin.as_view()'),
    path('api/mixins/courses/<str:pk>', views.CourseOtherMixin.as_view(), name='CourseOtherMixin.as_view()'),
]