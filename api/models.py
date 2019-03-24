from django.db import models


class Town(models.Model):
    region_code = models.PositiveSmallIntegerField()
    region_name = models.CharField(max_length=50)
    dept_code = models.CharField(max_length=3)
    distr_code = models.PositiveSmallIntegerField()
    code = models.IntegerField()
    name = models.CharField(max_length=50)
    population = models.PositiveIntegerField()
    average_age = models.FloatField()
