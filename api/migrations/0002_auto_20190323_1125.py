import csv
import os

from api.models import Town

from django.db import migrations
from django.conf import settings


def upload_csv(apps, schema_editor):
    filename = os.path.join(settings.BASE_DIR, 'data/French Towns Data.csv')
    with open(filename) as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i > 1:
                _, created = Town.objects.get_or_create(
                    region_code=row[0],
                    region_name=row[1],
                    dept_code=row[2],
                    distr_code=row[3],
                    code=row[4],
                    name=row[5],
                    population=row[6],
                    average_age=row[7],
                )


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(upload_csv),
    ]
