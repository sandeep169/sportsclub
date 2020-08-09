# Generated by Django 3.0.3 on 2020-03-07 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_delete_testint'),
    ]

    operations = [
        migrations.CreateModel(
            name='testint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.IntegerField()),
                ('total_blnull', models.IntegerField(blank=True, null=True)),
                ('total_null', models.IntegerField(blank=True)),
                ('totaldef', models.IntegerField(blank=True, default=1)),
            ],
        ),
    ]