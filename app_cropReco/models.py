from django.db import models

# Create your models here.
class Crop_models(models.Model):
    Nitrogen = models.IntegerField(default=0)
    Phosphorus = models.IntegerField(default=0)
    Potassium= models.IntegerField(default=0)
    Temperature= models.IntegerField(default=0)
    Humidity= models.IntegerField(default=0)
    pH= models.IntegerField(default=0)
    Rainfall= models.IntegerField(default=0)
    #recommendation model
    Crop_reco=models.TextField(blank=True, null=True)