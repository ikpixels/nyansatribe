# Generated by Django 4.2.2 on 2023-07-03 00:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_nation', '0002_alter_album_uploaded_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='uploaded_on',
            field=models.DateField(default=datetime.datetime(2023, 7, 3, 0, 23, 49, 671532, tzinfo=datetime.timezone.utc)),
        ),
    ]