import csv
from datetime import datetime

from django.conf import settings
from django.contrib.gis.geos import Point
from django.core.management.base import BaseCommand

from food.models import FoodTruck


class Command(BaseCommand):
    help = 'Import data from CSV file into FoodTruck model'

    def handle(self, *args, **options):
        self.import_food_trucks_from_csv(settings.FOOD_TRUCK_DATA_FILE)

    def convert_date_time(self, date_str):
        # Convert date string to a datetime object
        try:
            return datetime.strptime(date_str, '%m/%d/%Y %I:%M:%S %p')
        except ValueError:
            return None

    def convert_date(self, date_str):
        try:
            return datetime.strptime(date_str, '%Y%m%d')
        except ValueError:
            return None

    def import_food_trucks_from_csv(self, file_path):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Map Excel columns to Django model fields
                mapped_row = {
                    'location_id': row['locationid'],
                    'applicant': row['Applicant'],
                    'facility_type': row['FacilityType'],
                    'cnn': int(row['cnn']),
                    'location_description': row['LocationDescription'],
                    'address': row['Address'],
                    'block_lot': row['blocklot'],
                    'block': row['block'],
                    'lot': row['lot'],
                    'permit': row['permit'],
                    'status': row['Status'],
                    'food_items': row['FoodItems'],
                    'x': float(row['X']) if row['X'] else None,
                    'y': float(row['Y']) if row['Y'] else None,
                    'latitude': float(row['Latitude']),
                    'longitude': float(row['Longitude']),
                    'schedule': row['Schedule'],
                    'days_hours': row['dayshours'],
                    'noi_sent': row['NOISent'],
                    'approved': self.convert_date_time(row['Approved']),
                    'received': self.convert_date(row['Received']),
                    'prior_permit': row['PriorPermit'],
                    'expiration_date': self.convert_date_time(row['ExpirationDate']),
                    'location': Point(float(row['Latitude']), float(row['Longitude'])),
                    'fire_prevention_districts': int(row['Fire Prevention Districts'])
                    if row['Fire Prevention Districts'] else None,
                    'police_districts': int(row['Police Districts']) if row['Police Districts'] else None,
                    'supervisor_districts': int(row['Supervisor Districts']) if row['Supervisor Districts'] else None,
                    'zip_codes': int(row['Zip Codes']) if row['Zip Codes'] else None,
                    'neighborhoods_old': row['Neighborhoods (old)'],
                }

                # Use 'location_id' as the primary key
                location_id = mapped_row.pop('location_id')
                FoodTruck.objects.update_or_create(location_id=location_id, defaults=mapped_row)

        self.stdout.write(self.style.SUCCESS('Data import completed successfully.'))
