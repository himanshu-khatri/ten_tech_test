import csv

from django.core.management import BaseCommand

from inventory.models import Inventory


class Command(BaseCommand):

    help = "Loads data from csv to create inventory records"

    def add_arguments(self, parser):
        parser.add_argument('csv_file_name', type=str)

    def handle(self, *args, **kwargs):
        csv_file_name = kwargs["csv_file_name"]
        model_records = []
        with open(csv_file_name, "r",) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                model_records.append(
                    Inventory(
                        title=row["title"],
                        description=row["description"],
                        remaining_count=row["remaining_count"],
                        expiration_date = row["expiration_date"]
                    )
                )
        if model_records:
            Inventory.objects.bulk_create(model_records)