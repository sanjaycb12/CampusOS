from django.db import models


class Student(models.Model):
    DEPARTMENTS = [
        ("CSE", "Computer Science"),
        ("ECE", "Electronics and Communication"),
        ("EEE", "Electrical and Electronics"),
        ("ME", "Mechanical Engineering"),
        ("CE", "Civil Engineering"),
        ("IT", "Information Technology"),
    ]

    full_name = models.CharField(max_length=100)

    register_number = models.CharField(
        max_length=20,
        unique=True
    )

    roll_number = models.CharField(max_length=20)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    department = models.CharField(
        max_length=5,
        choices=DEPARTMENTS
    )

    semester = models.PositiveSmallIntegerField()

    admission_year = models.PositiveSmallIntegerField()

    date_of_birth = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} ({self.register_number})"
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    ROLE_CHOICES = (
        ('student', 'Student'),
        ('faculty', 'Faculty'),
        ('admin', 'Admin'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='student'
    )