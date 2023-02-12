from django.db import models


# Create your models here.
class PluckingRequirements(models.Model):
    total_ha = models.FloatField()
    total_days = models.FloatField()
    ha_day_target = models.FloatField()
    pluckers_req = models.FloatField()
    daily_actual = models.FloatField()

    def __str__(self):
        return self.total_ha


class PluckingRounds(models.Model):
    today_date = models.DateTimeField()
    plucking_date = models.IntegerField()
    division = models.CharField(max_length=20, default=None)
    zone = models.CharField(max_length=20, default=None)
    field = models.IntegerField()
    plucking_days = models.IntegerField()
    plucking_rounds = models.IntegerField()

    def __str__(self):
        return self.today_date


class PluckingPlanner(models.Model):
    division_area = models.FloatField()
    vp_division_area = models.FloatField()
    sd_division_area = models.FloatField()
    vp_blocks_per_zone = models.FloatField()
    sd_blocks_per_zone = models.FloatField()
    vp_zone_size = models.FloatField()
    sd_zone_size = models.FloatField()
    vp_schemes_per_division = models.FloatField()
    sd_schemes_per_division = models.FloatField()
    vp_rounds_per_zone = models.FloatField()
    sd_rounds_per_zone = models.FloatField()
    total_working_days = models.FloatField()
    total_pluckers_per_division = models.FloatField()
    total_supervisors_per_division = models.FloatField()
    total_schemes_per_division = models.FloatField()
    public_holidays = models.FloatField()
    paydays = models.FloatField()

    def __str__(self):
        return self.division_area


class ProgrammedSchemePlucking(models.Model):
    leaf_quality = models.FloatField()
    VP_percentage = models.FloatField()
    SD_percentage = models.FloatField()
    VP_division_area = models.FloatField()
    SD_division_area = models.FloatField()
    field_spacing = models.FloatField()
    max_bag_kgs = models.IntegerField()
    plucker_grade = models.CharField(max_length=20, default=None)
    VP_lines = models.IntegerField()
    SD_lines = models.IntegerField()
    VP_line_bushes = models.IntegerField()
    SD_line_bushes = models.IntegerField()
    block_size = models.IntegerField()
    VP_scheme = models.IntegerField()
    SD_scheme = models.IntegerField()
    VP_pluckers_ha = models.IntegerField()
    SD_pluckers_ha = models.IntegerField()
    VP_scheme_day = models.IntegerField()
    SD_scheme_day = models.IntegerField()
    VP_rounds = models.IntegerField()
    SD_rounds = models.IntegerField()
    pluckers = models.IntegerField()
    zone_number = models.IntegerField()
    zone_number_pluckers = models.IntegerField()
    zone_number_supervisor = models.IntegerField()
    zone_schemes_Max_day = models.IntegerField()
    zone_scheme_moves_day = models.IntegerField()

    def __str__(self):
        return self.leaf_quality


class TeaPluckingPlannerSaveData(models.Model):
    division_area = models.FloatField()
    vp_percentage = models.FloatField()
    sd_percentage = models.FloatField()
    month = models.DateField()
    vp_division_area = models.FloatField()
    sd_division_area = models.FloatField()
    vp_blocks_per_zone = models.IntegerField()
    sd_blocks_per_zone = models.IntegerField()
    vp_zone_size = models.FloatField()
    sd_zone_size = models.FloatField()
    vp_schemes_per_division = models.IntegerField()
    sd_schemes_per_division = models.IntegerField()
    vp_rounds_per_zone = models.IntegerField()
    sd_rounds_per_zone = models.IntegerField()
    total_pluckers_per_division = models.IntegerField()
    total_supervisors_per_division = models.IntegerField()
    total_schemes_per_division = models.IntegerField()

    def __str__(self):
        return self.division_area