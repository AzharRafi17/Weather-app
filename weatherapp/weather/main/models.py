from django.db import models

class Cities(models.Model):
    city= models.CharField(max_length=100)

    def __str__(self) :
        return self.city