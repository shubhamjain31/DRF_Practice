from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.

# ------------------------------------------------- @ Simple API @ -----------------------------------------------
@csrf_exempt
def employeeListView(request, pk=None):
    if request.method == 'GET':
        employees   = Employee.objects.all()
        serializer  = EmployeeSerializer(employees, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data_           = JSONParser().parse(request)
        serializer      = EmployeeSerializer(data=data_)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)

    elif request.method == 'PUT':
        employee_obj    = Employee.objects.get(pk=pk)

        data_           = JSONParser().parse(request)
        serializer      = EmployeeSerializer(employee_obj, data=data_)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)

    elif request.method == 'DELETE':
        employee_obj    = Employee.objects.get(pk=pk)
        employee_obj.delete()

        return JsonResponse({}, status=204)

# ------------------------------------------------- @ APIView @ -----------------------------------------------
@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def employeeListAPIView(request, pk=None):
    if request.method == 'GET':
        if pk is None or pk == 'None':
            employees   = Employee.objects.all()
        else:
            employees   = Employee.objects.filter(pk=pk)
        serializer  = EmployeeSerializer(employees, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        # data_           = JSONParser().parse(request)
        serializer      = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    elif request.method == 'PUT':
        employee_obj    = Employee.objects.get(pk=pk)

        serializer      = EmployeeSerializer(employee_obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    elif request.method == 'PATCH':
        employee_obj    = Employee.objects.get(pk=pk)

        serializer      = EmployeeSerializer(employee_obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    elif request.method == 'DELETE':
        employee_obj    = Employee.objects.get(pk=pk)
        employee_obj.delete()

        return Response({}, status=204)