from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Prediction(models.Model):
    State = models.CharField(max_length=122)
    Avg   = models.IntegerField(default=1)
    Max   = models.IntegerField()
    Min   = models.IntegerField()
    Pollutants = models.CharField(max_length=122)
    def save(self, *args, **kwargs):
        super(Prediction, self).save(*args, **kwargs)
    
  
        
       