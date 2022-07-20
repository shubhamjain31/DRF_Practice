from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('viewset/courses', views.CourseOListViewSet, basename='course')
router.register('modelviewset/courses', views.CourseOListModelViewSet, basename='course')

urlpatterns = [
    # path('api/simple/employees/<str:pk>', views.employeeListView, name='employeeListView'),
    path('api/apiview/courses/<str:pk>', views.CourseListAPIView.as_view(), name='CourseListAPIView.as_view()'),
    path('api/apiview/courses', views.CourseListAPIView.as_view(), name='CourseListAPIView.as_view()'),

    path('api/mixins/courses', views.CourseListMixin.as_view(), name='CourseListMixin.as_view()'),
    path('api/mixins/courses/<str:pk>', views.CourseOtherMixin.as_view(), name='CourseOtherMixin.as_view()'),

    path('api/generic/courses', views.CourseOListGenericView.as_view(), name='CourseOListGenericView.as_view()'),
    path('api/generic/courses/<str:pk>', views.CourseOListGenericView.as_view(), name='CourseOListGenericView.as_view()'),

    path('api/all/generic/courses', views.CourseOListAllGenericView.as_view(), name='CourseOListAllGenericView.as_view()'),
    path('api/all/generic/courses/<str:pk>', views.CourseOListAllGenericView.as_view(), name='CourseOListAllGenericView.as_view()'),

    path('api/', include(router.urls))
]