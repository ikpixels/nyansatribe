# Generated by Django 4.2.2 on 2023-07-24 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0005_alter_product_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='number_of_tickets',
        ),
        migrations.RemoveField(
            model_name='product',
            name='ticket',
        ),
        migrations.RemoveField(
            model_name='product',
            name='ticketCategory',
        ),
        migrations.RemoveField(
            model_name='product',
            name='time',
        ),
        migrations.RemoveField(
            model_name='product',
            name='venue',
        ),
        migrations.RemoveField(
            model_name='product',
            name='vipPrice',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=18),
        ),
        migrations.DeleteModel(
            name='ticketsCategory',
        ),
    ]