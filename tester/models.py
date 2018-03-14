from django.db import models

class ColourCombo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    bgcolour_one = models.CharField(max_length=7, default='#FF5733')
    bgcolour_two = models.CharField(max_length=7, default='#E58571')
    textcolour_one = models.CharField(max_length=7, default='#000000')
    textcolour_two = models.CharField(max_length=7, default='#000000')

    def __str__(self):
        return "Background1 - {},  Background2 - {}".format(self.bgcolour_one, 
                                                            self.bgcolour_two)