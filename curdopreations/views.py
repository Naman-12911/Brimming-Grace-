from django.shortcuts import render
from rest_framework.views import APIView
from .models import Employee
from .serializers import employeeSerializer
from django.http.response import Http404
from rest_framework.response import Response
# Create your views here.

class employeeAPIView(APIView):
    
        # READ a employee
        def get_object(self, pk):
            try:
                return Employee.objects.get(pk=pk)
            except Employee.DoesNotExist:
                raise Http404
        # get the employee by id otherwise all the employee
        def get(self, request, pk=None, format=None):
            if pk:
                data = self.get_object(pk)
                serializer = employeeSerializer(data)
                return Response(serializer.data)

            else:
                data = Employee.objects.all()
                serializer = employeeSerializer(data, many=True)

                return Response(serializer.data)
        # create the employee
        def post(self, request, format=None):
            data = request.data
            serializer = employeeSerializer(data=data)

            # Check if the data passed is valid
            serializer.is_valid(raise_exception=True)

            # Create employee in the DB
            serializer.save()

            # Return Response to User

            response = Response()

            response.data = {
                'message': 'employee Created Successfully',
                'data': serializer.data
            }

            return response
        # update the employee
        def put(self, request, pk=None, format=None):
                # Get the todo to update
            todo_to_update = Employee.objects.get(pk=pk)

            # Pass the instance to update to the serializer, and the data and also partial to the serializer
            # Passing partial will allow us to update without passing the entire employee object
            serializer = employeeSerializer(instance=todo_to_update,data=request.data, partial=True)

            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = Response()

            response.data = {
                'message': 'employee Updated Successfully',
                'data': serializer.data
            }

            return response
        # delete the employee
        def delete(self, request, pk, format=None):
            emp_to_delete =  Employee.objects.get(pk=pk)

            # delete the todo
            emp_to_delete.delete()

            return Response({
                'message': 'employee Deleted Successfully'
            })
