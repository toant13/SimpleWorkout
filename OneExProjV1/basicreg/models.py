from django.db import models

# Create your models here.


class Lift(models.Model):
    lift_name = models.CharField(max_length=50)
    numberofsets = models.IntegerField(default=0)
    numberofreps = models.IntegerField(default=0)
    percentage = models.IntegerField(default=0)

    def __unicode__(self):
        return self.lift_name

class Regiment(models.Model):
    regiment_name = models.CharField(max_length=50)
    lifts = models.ManyToManyField(Lift)
    
    def __unicode__(self):
        return self.regiment_name