# Generated by Django 3.0.3 on 2020-03-09 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tournament', '0010_auto_20200309_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badminton',
            name='tour_img',
            field=models.ImageField(blank=True, upload_to='badminton/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='chess',
            name='tour_img',
            field=models.ImageField(blank=True, upload_to='chess/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='cricket',
            name='tour_img',
            field=models.ImageField(blank=True, upload_to='cricket/%Y/%m/%d/'),
        ),
    ]
