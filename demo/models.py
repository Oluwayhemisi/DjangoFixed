from django.db import models


# Create your models here.
class House(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)

    def __str__(self):
        return self.house.name
