# Generated by Django 4.2.2 on 2023-07-24 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0002_ticketscategory_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets_order',
            name='ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='Event.ticket'),
        ),
    ]
