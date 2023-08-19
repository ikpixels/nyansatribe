# Generated by Django 4.2.2 on 2023-07-03 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_alter_product_ticketcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='payment_method',
            field=models.CharField(choices=[('TNM', 'Mpamba'), ('Airtel', 'Aitel Money'), ('NB', 'National Bank')], max_length=20, null=True),
        ),
    ]
