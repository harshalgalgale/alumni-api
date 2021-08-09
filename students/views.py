import logging
import string
from datetime import datetime
import random

import pandas as pd
from django.contrib.auth import get_user_model

from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from members.models import PersonalProfile
from students.models import Student
from students.serializers import StudentSerializer

User = get_user_model()


def generate_random_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join((random.choice(chars)) for x in range(20))


def process_students_data_file(full_file_path):
    logging.info(msg='Reading inputs')
    student_data = pd.read_csv(full_file_path)
    for row_index in student_data.index:
        reg_no=student_data['reg_no'][row_index]
        birth_date=student_data['birth_date'][row_index]
        birth_date = datetime.strptime(birth_date, '%d/%m/%Y').date()
        first_name=student_data['first_name'][row_index]
        middle_name=student_data['middle_name'][row_index]
        last_name=student_data['last_name'][row_index]
        degree=student_data['degree'][row_index]
        department=student_data['department'][row_index]
        reg_year=int(student_data['reg_year'][row_index])
        pass_year=int(student_data['grad_year'][row_index])
        gender=student_data['gender'][row_index]
        email=student_data['email'][row_index]
        contact=student_data['contact'][row_index]
        student = {
            'reg_no': reg_no,
            'birth_date': birth_date,
            'first_name':first_name,
            'middle_name': middle_name,
            'last_name': last_name,
            'degree': degree.lower().replace(' ', ''),
            'department': department,
            'reg_year': reg_year,
            'pass_year': pass_year,
            'gender': gender[0]
        }
        student = Student.objects.create(**student)
        if email:
            username = f'{first_name}{last_name}'
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=generate_random_password())
            user.name = f'{first_name} {last_name}'
            user.save()

            member = {
                'user': user,
                'first_name': first_name,
                'middle_name': middle_name,
                'last_name': last_name,
                'gender': gender[0],
                'student': student,
                'birth_date': student.birth_date,
                'phone': contact
            }
            member = PersonalProfile.objects.create(**member)


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated,)


class BatchUploadStudentsView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def put(self, request, *args, **kwargs):
        students_data_file = request.FILES.get('file')
        with students_data_file.file as csv_file:
            process_students_data_file(csv_file)
        return Response(status=204)
