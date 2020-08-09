from django.db import models

# Create your models here.
#this will create table in database "polldb" with name Home_Destination
class Destination(models.Model):
        name = models.CharField(max_length=50)
        img = models.ImageField(upload_to='pics') #for media we will join base dir with media in setting and pass url in media_url
        desc = models.TextField()
        def __str__(self):
                return f"{self.name}"

