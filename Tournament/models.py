from django.db import models

# Create your models here.


class TableTennis(models.Model):
        tour_name = models.CharField(max_length=100)
        venue = models.TextField()
        tour_start_date = models.DateField()
        reg_close_date = models.DateField()
        organiser_name = models.TextField()
        prize = models.TextField()
        description = models.TextField(blank=True)
        total_team = models.IntegerField(blank=True,null=True)
        tour_img = models.ImageField(upload_to='tableTennis/%Y/%m/%d/',blank=True)

class Chess(models.Model):
        tour_name = models.CharField(max_length=100)
        venue = models.TextField()
        tour_start_date = models.DateField()
        reg_close_date = models.DateField()
        organiser_name = models.TextField()
        prize = models.TextField()
        description = models.TextField(blank=True)
        total_team = models.IntegerField(blank=True, null=True)
        tour_img = models.ImageField(upload_to='chess/%Y/%m/%d/',blank=True)


class Cricket(models.Model):
        tour_name = models.CharField(max_length=100)
        venue = models.TextField()
        tour_start_date = models.DateField()
        reg_close_date = models.DateField()
        organiser_name = models.TextField()
        prize = models.TextField()
        description = models.TextField(blank=True)
        total_team = models.IntegerField(blank=True, null=True)
        tour_img = models.ImageField(upload_to='cricket/%Y/%m/%d/',blank=True)


class Badminton(models.Model):
        tour_name = models.CharField(max_length=100)
        venue = models.TextField()
        tour_start_date = models.DateField()
        reg_close_date = models.DateField()
        organiser_name = models.TextField()
        prize = models.TextField()
        description = models.TextField(blank=True)
        total_team = models.IntegerField(blank=True, null=True)
        tour_img = models.ImageField(upload_to='badminton/%Y/%m/%d/',blank=True)