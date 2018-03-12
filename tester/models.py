from django.db import models

class ColourCombo(models.Model):
    bgcolour_one = models.CharField(max_length=7)
    bgcolour_two = models.CharField(max_length=7)
    textcolour_one = models.CharField(max_length=7)
    textcolour_two = models.CharField(max_length=7)