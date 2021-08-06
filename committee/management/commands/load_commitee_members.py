import csv
import logging
import os

from django.core.management import BaseCommand
from collections import OrderedDict as od
from committee.models import CommitteeMember
from members.models import PersonalProfile

POSITION = [
    ('PR', 'President'),
    ('VP', 'Vice President'),
    ('SC', 'Secretary'),
    ('TR', 'Treasurer'),
    ('MB', 'Member'),
]


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
                committee_member = dict(row)
                member = PersonalProfile.objects.get(id=committee_member['id'])
                position_value = committee_member['position'].strip()
                position = POSITION[list(od(POSITION).values()).index(position_value)][0]
                CommitteeMember(
                    member=member,
                    position=position
                ).save()
