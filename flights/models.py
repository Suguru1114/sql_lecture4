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

    # have to get to know how oto add the destination after migrate the file fo the destination 
    # it would be, can i migrate after migrate and just change the 1 line and mighrate again   

    def __str__(self):
        return f"{self.id}:{self.origin.code} to {self.destination}"