import logging
import os

from django.core.management import BaseCommand

from students.views import process_students_data_file


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--filepath', default=None, type=str)

    def handle(self, *args, **options):
        filepath = options['filepath']

        if not filepath:
            filepath = input('No Filepath given in argument. Please enter full path of file: ')

        if os.path.exists(filepath):
            process_students_data_file(filepath)
        else:
            error_message = 'File not found. File name: %s' % filepath
            logging.error(msg=error_message)
