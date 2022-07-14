from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer

# Create your views here.

class CourseListAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            course          = self.get_course(pk)
            serializer      = CourseSerializer(course)
        else:
            courses         = Course.objects.all()
            serializer      = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request, pk=None):
        serializer      = CourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def get_course(self, pk=None):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(status = status.HTTP_204_NO_CONTENT)
    
    def delete(self, request, pk=None):
        self.get_course(pk).delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        
    def put(self, request, pk=None):
        course              = self.get_course(pk)
        courseSerializer    = CourseSerializer(course, data=request.data)

        if courseSerializer.is_valid():
            courseSerializer.save()

            return Response(courseSerializer.data)
        return Response(courseSerializer.errors)