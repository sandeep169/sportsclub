# Generated by Django 3.0.3 on 2020-03-09 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tournament', '0006_badminton_chess_cricket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='badminton',
            old_name='event_img',
            new_name='tour_img',
        ),
        migrations.RenameField(
            model_name='chess',
            old_name='event_img',
            new_name='tour_img',
        ),
        migrations.RenameField(
            model_name='cricket',
            old_name='event_img',
            new_name='tour_img',
        ),
    ]
