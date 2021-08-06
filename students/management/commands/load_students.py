import csv
import logging
import os

from django.core.management import BaseCommand

from students.models import Student


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--filepath', default=None, type=str)

    def handle(self, *args, **options):
        filepath = options['filepath']

        if not filepath:
            filepath = input('No Filepath given in argument. Please enter full path of file: ')

        if os.path.exists(filepath):
            self.process_file(filepath)
        else:
            error_message = 'File not found. File name: %s' % filepath
            logging.error(msg=error_message)

    def process_file(self, full_file_path):
        logging.info(msg='Reading inputs')
        with open(full_file_path, 'r') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                student_data = dict(row)
                Student(
                    reg_no=student_data['reg_no'],
                    birth_date=student_data['birth_date'].strip(),
                    first_name=student_data['first_name'].strip(),
                    middle_name=student_data['middle_name'].strip(),
                    last_name=student_data['last_name'].strip(),
                    degree=student_data['degree'].strip(),
                    department=student_data['department'].strip(),
                    reg_year=int(student_data['reg_year'].strip()),
                    pass_year=int(student_data['pass_year'].strip()),
                    gender=student_data['gender'].strip()
                ).save()
