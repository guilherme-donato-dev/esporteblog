from django.db import models

# Create your models here.
class Player(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True)
    team = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(null=True, blank=True)
    goals = models.IntegerField(null=True, blank=True)
    assists = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    

