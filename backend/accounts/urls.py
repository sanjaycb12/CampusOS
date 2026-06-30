from django.urls import path

from .views import (
    StudentListAPIView,
    StudentDetailAPIView,ProfileAPIView
)

urlpatterns = [

    path(
        'students/',
        StudentListAPIView.as_view(),
        name='students'
    ),

    path(
        'students/<int:pk>/',
        StudentDetailAPIView.as_view(),
        name='student-detail'
    ),
    path(
        'profile/',
        ProfileAPIView.as_view()
    ),

]