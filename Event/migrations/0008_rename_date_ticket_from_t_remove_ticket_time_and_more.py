# Generated by Django 4.2.2 on 2023-08-18 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0007_alter_tickets_order_paid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='date',
            new_name='from_t',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='time',
        ),
        migrations.AddField(
            model_name='ticket',
            name='to_t',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
