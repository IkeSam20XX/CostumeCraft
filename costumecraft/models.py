from django.db import models

class Supply(models.Model):
    name = models.CharField(max_length=200)
    material = models.CharField(max_length=500)
    amount = models.CharField(max_length=10)
    source = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    use = models.CharField(max_length=500)

    def __str__(self):
        return  self.name


