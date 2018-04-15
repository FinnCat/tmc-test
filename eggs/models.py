from django.db import models

# Create your models here.
class Egg(models.Model):
    egg_code  = models.CharField(max_length=20)
    egg_name = models.CharField(max_length=150)
    base_color = models.CharField(max_length=20)
    ornament = models.CharField(max_length=25)
    picture = models.CharField(max_length=50)
    cooked = models.DateTimeField()
    best_before = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_fullname(self):
        return self.egg_code + ' '+ self.egg_name

    def __str__(self):
        return self.egg_code+' '+self.egg_name
