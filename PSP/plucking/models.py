from django.contrib.auth import admin
from django.db import models


# Create your models here.
class Resourcesexcell(models.Model):
    title = models.CharField(max_length=500)
    file = models.FileField(upload_to='uploads/resources/')
    image_url = models.URLField(max_length=500)

    def __str__(self):
        return self.title


class Resources(models.Model):
    description = models.CharField(max_length=200)
    file = models.FileField(upload_to='uploads/resources/')

    def __str__(self):
        return self.description


class DataEntry(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()


class ProgrammedScheme(models.Model):
    plucking_date = models.DateField(auto_now=True, blank=False, null=False)
    leaf_quality = models.DecimalField(max_digits=6, decimal_places=2)
    VP_percentage = models.DecimalField(max_digits=6, decimal_places=2)
    SD_percentage = models.DecimalField(max_digits=6, decimal_places=2)
    division_area = models.DecimalField(max_digits=6, decimal_places=2)
    VP_division_area = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    SD_division_area = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    block_size = models.IntegerField()
    VP_scheme = models.IntegerField()
    SD_scheme = models.IntegerField()
    VP_pluckers_ha = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    SD_pluckers_ha = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    VP_rounds = models.IntegerField()
    SD_rounds = models.IntegerField()
    zone_number_supervisor = models.IntegerField()
    VP_plucked_area_day = models.DecimalField(max_digits=6, decimal_places=2)
    SD_plucked_area_day = models.DecimalField(max_digits=6, decimal_places=2)
    VP_zone_size = models.DecimalField(max_digits=6, decimal_places=2)
    SD_zone_size = models.DecimalField(max_digits=6, decimal_places=2)
    VP_zone_number_pluckers = models.DecimalField(max_digits=6, decimal_places=2)
    SD_zone_number_pluckers = models.DecimalField(max_digits=6, decimal_places=2)
    total_number_pluckers = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.item} - {str(self.leaf_quality)}"


class RoundsMonitor(models.Model):
    today_date = models.DateField(auto_now_add=True, blank=False, null=False)
    plucking_round = models.IntegerField()
    field = models.IntegerField()
    plucking_day = models.DateField(auto_now=False, blank=True, null=True)
    next_plucking = models.DateField(auto_now=False, blank=True, null=True)
    actual_plucking_day = models.DateField(auto_now=False, blank=True, null=True)
    days_behind = models.IntegerField()
    days_ahead = models.IntegerField()
    total_plucking_round = models.IntegerField()
    month_end = models.IntegerField()
    round_bal_days = models.IntegerField()
    days_to_end_month = models.IntegerField()
    days_bf = models.IntegerField()

    def __str__(self):
        return str(self.field)
