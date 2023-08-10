from django.db import models

# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city}:{self.code}"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="deprtures")
    destination = models.ForeignKey(Airport,on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField() 

    # use djangp admin app to input data 


    def __str__(self):
        return f"{self.id}:{self.origin.code} to {self.destination}"
    
class Passenger(models.Model):    
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    # def __str__(self):
    #     return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return f"{self.first} {self.last}"