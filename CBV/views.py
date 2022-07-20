from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.viewsets import ViewSet

from .models import Course
from .serializers import CourseSerializer

# Create your views here.

# ------------------------------------------------- @ APIView @ -----------------------------------------------

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

# ------------------------------------------------- @ Mixin View @ -----------------------------------------------
class CourseListMixin(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset            = Course.objects.all()
    serializer_class    = CourseSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class CourseOtherMixin(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset            = Course.objects.all()
    serializer_class    = CourseSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

# ------------------------------------------------- @ GenericView @ -----------------------------------------------
# 1st Way
class CourseOListGenericView(generics.ListAPIView, generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView, generics.RetrieveAPIView):
    queryset            = Course.objects.all()
    serializer_class    = CourseSerializer

# 2nd Way
class CourseOListAllGenericView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset            = Course.objects.all()
    serializer_class    = CourseSerializer

# ------------------------------------------------- @ ViewSet @ -----------------------------------------------
class CourseOListViewSet(ViewSet):
    def list(self, request):
        courses             = Course.objects.all()
        serializer          = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        try:
            courses             = Course.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer          = CourseSerializer(courses)
        return Response(serializer.data)

    def create(self, request):
        serializer          = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, pk):
        try:
            course             = Course.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer          = CourseSerializer(course)
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            course             = Course.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer          = CourseSerializer(course)
        return Response(serializer.data)