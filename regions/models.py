from django.db import models


class Continent(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    continent = models.ForeignKey(Continent, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    capital = models.CharField(max_length=100, null=True)
    language = models.CharField(max_length=100, null=True)
    population = models.IntegerField(null=True)
    area = models.FloatField(null=True)

    def __str__(self):
        return self.name
