# Generated by Django 4.2.2 on 2023-08-18 19:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_nation', '0017_alter_album_uploaded_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='uploaded_on',
            field=models.DateField(default=datetime.datetime(2023, 8, 18, 19, 52, 19, 525575, tzinfo=datetime.timezone.utc)),
        ),
    ]