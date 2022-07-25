from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('viewset/courses', views.CourseListViewSet, basename='course')
router.register('modelviewset/courses', views.CourseListModelViewSet, basename='course')

urlpatterns = [
    # path('api/simple/employees/<str:pk>', views.employeeListView, name='employeeListView'),
    path('api/apiview/courses/<str:pk>', views.CourseListAPIView.as_view(), name='CourseListAPIView'),
    path('api/apiview/courses', views.CourseListAPIView.as_view(), name='CourseListAPIView'),

    path('api/mixins/courses', views.CourseListMixin.as_view(), name='CourseListMixin'),
    path('api/mixins/courses/<str:pk>', views.CourseOtherMixin.as_view(), name='CourseOtherMixin'),

    path('api/generic/courses', views.CourseOListGenericView.as_view(), name='CourseOListGenericView'),
    path('api/generic/courses/<str:pk>', views.CourseOListGenericView.as_view(), name='CourseOListGenericView'),

    path('api/all/generic/courses', views.CourseOListAllGenericView.as_view(), name='CourseOListAllGenericView'),
    path('api/all/generic/courses/<str:pk>', views.CourseOListAllGenericView.as_view(), name='CourseOListAllGenericView'),

    path('api/', include(router.urls)),

    path('api/instructor', views.InstructorListModelViewSet.as_view(), name='InstructorListModelViewSet'),
    path('api/instructor/<str:pk>', views.InstructorListModelViewSet.as_view(), name='InstructorListModelViewSet'),

    path('api/subject', views.SubjectListModelViewSet.as_view(), name='SubjectListModelViewSet'),
    path('api/subject/<str:pk>', views.SubjectListModelViewSet.as_view(), name='SubjectListModelViewSet'),

    path('api/subject/details/<int:pk>', views.SubjectDetailHyperLinkedModel.as_view(), name='subject-details'),
    path('api/instructor/details/<int:pk>', views.InstructorDetailHyperLinkedModel.as_view(), name='instructor-detail'),
]