# Generated by Django 4.2.2 on 2023-07-20 10:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music_nation', '0005_alter_album_uploaded_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_genre',
            field=models.CharField(choices=[('House', 'House'), ('Hip Hop', 'Hip hop'), ('Trap', 'Trap'), ('Raggie', 'Raggie'), ('Amapiano', 'Amapiano'), ('Gospel', 'Gospel'), ('Beats', 'Beats'), ('Afro House', 'Afro House'), ('Dancehall', 'Dancehall'), ('Poetry', 'Poetry/Poem'), ('Rock', 'Rock')], default='Rock', max_length=30),
        ),
        migrations.AlterField(
            model_name='album',
            name='uploaded_on',
            field=models.DateField(default=datetime.datetime(2023, 7, 20, 10, 37, 3, 270718, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Podcasts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('youtubelink', embed_video.fields.EmbedVideoField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='podcast', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
