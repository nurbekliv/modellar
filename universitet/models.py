from django.db import models


# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Fakultet(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Fanlar(models.Model):
    name = models.CharField(max_length=100)
    fakult = models.ForeignKey(Fakultet, on_delete=models.CASCADE)