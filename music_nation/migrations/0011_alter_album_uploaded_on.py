# Generated by Django 4.2.2 on 2023-07-24 00:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_nation', '0010_alter_album_uploaded_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='uploaded_on',
            field=models.DateField(default=datetime.datetime(2023, 7, 24, 0, 40, 44, 984523, tzinfo=datetime.timezone.utc)),
        ),
    ]
