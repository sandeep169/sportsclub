# Generated by Django 3.0.3 on 2020-03-07 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_testint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testint',
            name='team',
        ),
        migrations.RemoveField(
            model_name='testint',
            name='total_blnull',
        ),
        migrations.RemoveField(
            model_name='testint',
            name='total_null',
        ),
        migrations.RemoveField(
            model_name='testint',
            name='totaldef',
        ),
        migrations.AddField(
            model_name='testint',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]