from django.db import models

# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id}:{self.origin} to {self.destination}"

class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=100, default='Default Destination')
    duration = models.IntegerField()
    #   55;03

    # have to get to know how oto add the destination after migrate the file fo the destination 
    # it would be, can i migrate after migrate and just change the 1 line and mighrate again   

    def __str__(self):
        return f"{self.id}:{self.origin} to {self.destination}"