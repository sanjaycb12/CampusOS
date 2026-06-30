from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializers import StudentSerializer
from .permissions import (
    IsAdmin,
    IsFaculty,
    IsStudent
)
class StudentListAPIView(APIView):

    permission_classes = [IsAuthenticated,IsAdmin]

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
    permission_classes = [IsAuthenticated,IsAdmin]

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

            return Response(
    serializer.errors,
    status=status.HTTP_400_BAD_REQUEST
)
    def delete(self, request, pk):

      student = Student.objects.get(pk=pk)

      student.delete()

      return Response(

        {"message": "Student deleted successfully"},

       status=status.HTTP_204_NO_CONTENT

    )
class ProfileAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user

        groups = [
            group.name
            for group in user.groups.all()
        ]

        return Response({

            "username": user.username,

            "email": user.email,

            "groups": [
                g.name
                for g in user.groups.all()
            ]

        })
class FacultyDashboardAPIView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsFaculty
    ]

    def get(self, request):

        students = Student.objects.all()

        serializer = StudentSerializer(
            students,
            many=True
        )

        return Response(serializer.data)