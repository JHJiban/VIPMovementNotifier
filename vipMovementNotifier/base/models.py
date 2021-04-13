from django.db import models

class VipMovement(models.Model):
    location=models.CharField(max_length=250)
    road=models.CharField(max_length=150)
    time=models.DateTimeField()

    def __str__(self):
        return self.location



