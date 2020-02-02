from django.db import models

class Car(models.Model):
    manufacturer = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    release_year = models.IntegerField()

    TRANSMISSION_CHOICES = [(1, 'Mechanics'), 
                            (2, 'Automatic'), 
                            (3, 'Robot')]

    transmission = models.IntegerField(choices=TRANSMISSION_CHOICES)
    color = models.CharField(max_length=25)