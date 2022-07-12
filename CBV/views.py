from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer

# Create your views here.

class CourseListAPIView(APIView):
    def get(self, request):
        courses         = Course.objects.all()
        serializer      = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer      = CourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)