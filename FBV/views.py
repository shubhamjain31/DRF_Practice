from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.

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