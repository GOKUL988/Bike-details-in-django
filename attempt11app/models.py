from django.db import models

# Create your models here.
class bike(models.Model):
    bikename=models.CharField(max_length=100)
    bikeserial=models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')