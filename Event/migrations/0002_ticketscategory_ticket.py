# Generated by Django 4.2.2 on 2023-07-24 00:34

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ticketsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=40)),
                ('simple_discription', models.CharField(max_length=40)),
                ('number_of_tickets', models.PositiveIntegerField(default=0)),
                ('district', models.CharField(choices=[('Balaka', 'Balaka'), ('Blantyre', 'Blantyre'), ('Chikwawa', 'Chikwawa'), ('Chiradzuru', 'Chiradzuru'), ('Chitipa', 'Chitipa'), ('Dedza', 'Dedza'), ('Dowa', 'Dowa'), ('Karonga', 'Karonga'), ('Kasungu', 'Kasungu'), ('Likoma', 'Likoma'), ('Lilongwe', 'Lilongwe'), ('Machinga', 'Machinga'), ('Mangochi', 'Mangochi'), ('Mchinji', 'Mchinji'), ('Mulanje', 'Mulanje'), ('Mwanza', 'Mwanza'), ('Mzimba', 'Mzimba'), ('Neno', 'Neno'), ('Nkhata_Bay', 'Nkhata_Bay'), ('Nkhotakota', 'Nkhotakota'), ('Nsanje', 'Nsanje'), ('Ntcheu', 'Ntcheu'), ('Ntchisi', 'Ntchisi'), ('Phalombe', 'Phalombe'), ('Ruphi', 'Ruphi'), ('Salima', 'Salima'), ('Thyolo', 'Thyolo'), ('Zomba', 'Zomba'), ('Others', 'Others')], default='Mwanza', max_length=40)),
                ('venue', models.CharField(blank=True, max_length=40, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('date', models.CharField(blank=True, max_length=40, null=True)),
                ('regular_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=18)),
                ('vip_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=18)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('youtube_video_link', embed_video.fields.EmbedVideoField(blank=True, null=True)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product_image/')),
                ('product_image2', models.ImageField(blank=True, null=True, upload_to='product_image/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ticketCategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Event.ticketscategory')),
            ],
            managers=[
                ('ticketObjects', django.db.models.manager.Manager()),
            ],
        ),
    ]
