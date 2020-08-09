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

        def __str__(self):
                return f"{self.tour_name}"

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

        def __str__(self):
                return f"{self.tour_name}"


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

        def __str__(self):
                return f"{self.tour_name}"


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

        def __str__(self):
                return f"{self.tour_name}"

class Participation(models.Model):
        p_name = models.CharField(max_length=100)
        p_age = models.IntegerField()
      #  p_gender = models.Choices()
        p_add = models.TextField()
        p_ph_no = models.IntegerField()
        def __str__(self):
                return f"{self.p_name}"
