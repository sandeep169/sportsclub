# Generated by Django 3.0.3 on 2020-03-07 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='offer',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='price',
        ),
        migrations.AddField(
            model_name='destination',
            name='blank1',
            field=models.TextField(blank=True, default='BLANK', max_length=50),
        ),
        migrations.AddField(
            model_name='destination',
            name='blank2',
            field=models.TextField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='destination',
            name='char1',
            field=models.TextField(default='NULL', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='char2',
            field=models.TextField(default='null', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='char3',
            field=models.TextField(default='Null', max_length=50, null=True),
        ),
    ]
