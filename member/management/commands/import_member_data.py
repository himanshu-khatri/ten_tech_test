import csv

from django.core.management import BaseCommand
from member.models import Member


class Command(BaseCommand):

    help = "Loads data from csv to create member records"

    def add_arguments(self, parser):
        parser.add_argument('csv_file_name', type=str)

    def handle(self, *args, **kwargs):
        csv_file_name = kwargs["csv_file_name"]
        model_records = []
        with open(csv_file_name, "r",) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                model_records.append(
                    Member(
                        name=row["name"],
                        surname=row["surname"],
                        booking_count=row["booking_count"],
                        date_joined = row["date_joined"]
                    )
                )
        if model_records:
            Member.objects.bulk_create(model_records)