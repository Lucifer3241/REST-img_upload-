from django.db import models

# Create your models here.

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Airport(models.Model):
    AirportName=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    State=models.CharField(max_length=100)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    
    def __str__(self):
        return self.AirportName



