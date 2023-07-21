from django.db import models

# Create your models here.
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=100, default='Default Destination')
    duration = models.IntegerField()
    #   55;03

    # have to get to know how oto add the destination after migrate the file fo the destination 
    # it would be, can i migrate after migrate and just change the 1 line and mighrate again 