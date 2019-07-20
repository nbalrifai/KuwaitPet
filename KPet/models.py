from django.db import models

class Pet (models.Model):
	name = models.CharField(max_length = 100)
	age = models.CharField(max_length = 2)
	available = models.TextField(null = True)
	description = models.CharField(max_length = 200)
	image = models.ImageField (null = True, blank = True)
	price = models.DecimalField (max_digits = 4, decimal_places = 2) 
def __str__(self):
    	return self.name