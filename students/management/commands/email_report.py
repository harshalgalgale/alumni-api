from datetime import timedelta, time, datetime

from django.core.mail import mail_admins
from django.core.mail import send_mail
from django.core.management import BaseCommand
from django.utils import timezone
from django.utils.timezone import make_aware

from config.settings import DEFAULT_FROM_EMAIL
from students.models import Student

today = timezone.now()
tomorrow = today + timedelta(1)
today_start = make_aware(datetime.combine(today, time()))
today_end = make_aware(datetime.combine(tomorrow, time()))


class Command(BaseCommand):
    help = "Send Today's Orders Report to Admins"

    def handle(self, *args, **options):
        students = Student.objects.all()

        if students:
            message = ""

            for student in students:
                message += f"{student} \n"

            subject = (
                f"Report for {today_start.strftime('%Y-%m-%d')} "
                f"to {today_end.strftime('%Y-%m-%d')}"
            )

            mail_admins(subject=subject, message=message, html_message=None)
            send_mail(
                subject='Subject here',
                message='Here is the message.',
                from_email=DEFAULT_FROM_EMAIL,
                recipient_list=['h.galgale@gmail.com'],
                fail_silently=False,
            )

            self.stdout.write("E-mail Report was sent.")
        else:
            self.stdout.write("No orders confirmed today.")
