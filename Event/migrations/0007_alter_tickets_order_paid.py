# Generated by Django 4.2.2 on 2023-07-24 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0006_ticket_ticket_booked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets_order',
            name='paid',
            field=models.CharField(choices=[('Approved', 'Paid'), ('Pending', 'Pending')], default='Pending', max_length=40),
        ),
    ]
