from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated 

class StudentListAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        students = Student.objects.all()

        serializer = StudentSerializer(
            students,
            many=True
        )

        return Response(serializer.data)
    def post(self, request):

        serializer = StudentSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
class StudentDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):

        student = Student.objects.get(pk=pk)

        serializer = StudentSerializer(student)

        return Response(serializer.data)


    def put(self, request, pk):

        student = Student.objects.get(pk=pk)

        serializer = StudentSerializer(

            student,

            data=request.data

        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(

            serializer.errors,

            status=400

        )
    def delete(self, request, pk):

      student = Student.objects.get(pk=pk)

      student.delete()

      return Response(

        {"message": "Student deleted successfully"},

        status=204

    )