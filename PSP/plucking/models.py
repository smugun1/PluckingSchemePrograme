from django.contrib.auth import admin
from django.db import models


# Create your models here.
class Resourcesexcell(models.Model):
    title = models.CharField(max_length=500)
    file = models.FileField(upload_to='uploads/resources/')
    image_url = models.URLField(max_length=500)

    def __str__(self):
        return self.title


class DataEntry(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()


class ProgrammedScheme(models.Model):
    plucking_date = models.DateField(auto_now=True, blank=False, null=False)
    leaf_quality = models.DecimalField(max_digits=6, decimal_places=2)
    VP_percentage = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    SD_percentage = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    division_area = models.DecimalField(max_digits=6, decimal_places=2)
    VP_division_area = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    SD_division_area = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    block_size = models.IntegerField()
    VP_scheme = models.IntegerField()
    SD_scheme = models.IntegerField()
    VP_pluckers_ha = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    SD_pluckers_ha = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
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


class FieldsToPluck(models.Model):
    Zone = models.CharField(max_length=100)
    Field_No = models.IntegerField()
    Leaf_Type = models.CharField(max_length=100, default=None)
    Ha = models.IntegerField(default=0.00)
    Days_to_plk = models.IntegerField()
    Prune_age = models.IntegerField()
    Number_of_schemes = models.IntegerField()
    Growing_days_CF = models.IntegerField()
    Month_day_01 = models.IntegerField()
    Month_day_02 = models.IntegerField()
    Month_day_03 = models.IntegerField()
    Month_day_04 = models.IntegerField()
    Month_day_05 = models.IntegerField()
    Month_day_06 = models.IntegerField()
    Month_day_07 = models.IntegerField()
    Month_day_08 = models.IntegerField()
    Month_day_09 = models.IntegerField()
    Month_day_10 = models.IntegerField()
    Month_day_11 = models.IntegerField()
    Month_day_12 = models.IntegerField()
    Month_day_13 = models.IntegerField()
    Month_day_14 = models.IntegerField()
    Month_day_15 = models.IntegerField()
    Month_day_16 = models.IntegerField()
    Month_day_17 = models.IntegerField()
    Month_day_18 = models.IntegerField()
    Month_day_19 = models.IntegerField()
    Month_day_20 = models.IntegerField()
    Month_day_21 = models.IntegerField()
    Month_day_22 = models.IntegerField()
    Month_day_23 = models.IntegerField()
    Month_day_24 = models.IntegerField()
    Month_day_25 = models.IntegerField()
    Month_day_26 = models.IntegerField()
    Month_day_27 = models.IntegerField()
    Month_day_28 = models.IntegerField()
    Month_day_29 = models.IntegerField()
    Month_day_30 = models.IntegerField()
    Month_day_31 = models.IntegerField()

    def __str__(self):
        return self.Field_No


class AutoFields(models.Model):
    Zone = models.CharField(max_length=100)
    Field_No = models.IntegerField()
    Leaf_type = models.CharField(max_length=100, default=None)
    Ha = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    Days_to_plk = models.IntegerField()
    Prune_age = models.IntegerField()
    Number_of_schemes = models.IntegerField()
    Growing_days_CF = models.IntegerField()
    Month_day_01 = models.IntegerField()
    Month_day_02 = models.IntegerField()
    Month_day_03 = models.IntegerField()
    Month_day_04 = models.IntegerField()
    Month_day_05 = models.IntegerField()
    Month_day_06 = models.IntegerField()
    Month_day_07 = models.IntegerField()
    Month_day_08 = models.IntegerField()
    Month_day_09 = models.IntegerField()
    Month_day_10 = models.IntegerField()
    Month_day_11 = models.IntegerField()
    Month_day_12 = models.IntegerField()
    Month_day_13 = models.IntegerField()
    Month_day_14 = models.IntegerField()
    Month_day_15 = models.IntegerField()
    Month_day_16 = models.IntegerField()
    Month_day_17 = models.IntegerField()
    Month_day_18 = models.IntegerField()
    Month_day_19 = models.IntegerField()
    Month_day_20 = models.IntegerField()
    Month_day_21 = models.IntegerField()
    Month_day_22 = models.IntegerField()
    Month_day_23 = models.IntegerField()
    Month_day_24 = models.IntegerField()
    Month_day_25 = models.IntegerField()
    Month_day_26 = models.IntegerField()
    Month_day_27 = models.IntegerField()
    Month_day_28 = models.IntegerField()
    Month_day_29 = models.IntegerField()
    Month_day_30 = models.IntegerField()
    Month_day_31 = models.IntegerField()

    def __str__(self):
        return self.Field_No

