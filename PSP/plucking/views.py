# Create a function from the above code to render an HTML template in Django views.py
import csv
from datetime import datetime, timedelta

import pandas as pd
from django.shortcuts import render, redirect

from .forms import PluckingForms, DataForm


def Home(request):
    context = {
        'name': {'This is the plucking reports Page'},
        'form': PluckingForms
    }
    return render(request, 'home.html', context)


def Plucking_scheme(request):
    context = {
        'name': {'This is the psp'},

    }
    return render(request, 'plucking_scheme.html', context)


# Create a function called tea_plucking_planner
def TeaPlucking_planner(request):
    # Define the variable

    current_datetime = datetime.now()
    vp_tea_area = 700  # m^2
    sd_tea_area = 900  # m^2
    pluckers_per_supervisor = 90  # Number of pluckers per supervisor
    supervisors_per_zone = 1  # Number of supervisors per zone
    schemes_per_day = 2  # Number of schemes per day
    max_moves_per_plucker_in_a_day = 2  # Max number of moves per plucker in a day
    vp_scheme_size = 350  # m^2
    sd_scheme_size = 450  # m^2
    block_size = 2500  # m^2
    vp_plucking_days = 8  # Number of days plucking (Plucking Days/Zone)
    sd_plucking_days = 9  # Number of days plucking (Plucking Days/Zone)
    vp_percentage = 0  # VP Percentage
    sd_percentage = 0  # Sd Percentage
    month = ""  # Selected month
    division_area = 0  # Division area
    vp_division_area = 0  # Initialize the vp_division_area variable
    sd_division_area = 0  # Initialize the sd_division_area variable

    # Calculate the number of blocks needed for a zone
    pluckers_per_block_vp = block_size / vp_tea_area
    pluckers_per_block_sd = block_size / sd_tea_area

    # POST request
    if request.method == "POST":
        # Get the data from the form
        division_area = float(request.POST.get("division_area", 0))  # Get with default value of 0
        vp_percentage = float(request.POST.get("vp_percentage", 0))
        sd_percentage = float(request.POST.get("sd_percentage", 0))
        month = request.POST.get("month", datetime.now().strftime("%B"))  # Set default to current month

        # Calculate the division area based on the input from user
        vp_division_area = vp_percentage / 100 * division_area
        sd_division_area = sd_percentage / 100 * division_area
        # division_area = vp_division_area + sd_division_area

        # Calculate the number of blocks needed for a zone based on the number of pluckers
        vp_blocks_per_zone = pluckers_per_supervisor * pluckers_per_block_vp
        sd_blocks_per_zone = pluckers_per_supervisor * pluckers_per_block_sd

        # Calculate the total area of a zone based on the number of blocks
        vp_zone_size = vp_blocks_per_zone * block_size / 10000
        sd_zone_size = sd_blocks_per_zone * block_size / 10000

        # Calculate the number of zones needed for a division based on the total area
        vp_schemes_per_division = vp_division_area * 10000 / vp_scheme_size
        sd_schemes_per_division = sd_division_area * 10000 / sd_scheme_size

        total_working_days = {
            "January": 31,
            "February": 28,
            "March": 31,
            "April": 30,
            "May": 31,
            "June": 30,
            "July": 31,
            "August": 31,
            "September": 30,
            "October": 31,
            "November": 30,
            "December": 31,
        }

        plucking_days = {

            "holidays": {
                "January": 1,
                "February": 0,
                "March": 0,
                "April": 3,
                "May": 1,
                "June": 2,
                "July": 0,
                "August": 0,
                "September": 0,
                "October": 2,
                "November": 0,
                "December": 3,
            },

            "paydays": {
                "January": 25,
                "February": 24,
                "March": 27,
                "April": 24,
                "May": 26,
                "June": 25,
                "July": 26,
                "August": 26,
                "September": 26,
                "October": 24,
                "November": 26,
                "December": 23,
            }
        }

        working_days_year = 313
        plucking_rounds_per_year = 36
        st_round_duration = working_days_year / plucking_rounds_per_year
        vp_round_duration = 8
        sd_round_duration = 9

        # Total working days considering public holidays and paydays
        total_working_days[month] = total_working_days[month] - plucking_days['holidays'][month]

        # Calculate the number of rounds needed for each zone considering public holidays and paydays
        vp_rounds_per_zone = total_working_days[month] / vp_round_duration
        sd_rounds_per_zone = total_working_days[month] / sd_round_duration

        # Total number of pluckers needed for the division
        total_pluckers_per_division = ((vp_schemes_per_division / vp_plucking_days) + (
                sd_schemes_per_division / sd_plucking_days)) / schemes_per_day

        # Total number of supervisors needed for the division
        total_supervisors_per_division = total_pluckers_per_division / 90

        # Total number of zones in the division
        total_schemes_per_division = vp_schemes_per_division + sd_schemes_per_division

        # save data
        data = [['VP Division Area', vp_division_area],
                ['SD Division Area', sd_division_area],
                ['VP Blocks per Zone', vp_blocks_per_zone],
                ['SD Blocks per Zone', sd_blocks_per_zone],
                ['VP Zone Size', vp_zone_size],
                ['SD Zone Size', sd_zone_size],
                ['VP Schemes per Division', vp_schemes_per_division],
                ['SD Schemes per Division', sd_schemes_per_division],
                ['Total Working Days', total_working_days[month]],
                ['VP Rounds per Zone', vp_rounds_per_zone],
                ['SD Rounds per Zone', sd_rounds_per_zone],
                ['Total Pluckers per Division', total_pluckers_per_division],
                ['Total Supervisors per Division', total_supervisors_per_division],
                ['Total Schemes per Division', total_schemes_per_division]]

        with open('data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)

        # Render the HTML page with the data
        context = {
            "data": data
        }
        return render(request, "teaPlucking_planner.html", context)

    # GET request
    else:
        return render(request, "teaPlucking_planner.html")


def TeaPlucking_planner_save_data(request):
    if request.method == 'POST':
        form = DataForm(request.POST)

        if form.is_valid():
            form.save()
            data = form.cleaned_data
            data_dict = {
                'division_area': data['division_area'],
                'VP_percentage': data['VP_percentage'],
                'SD_percentage': data['SD_percentage'],
                'month': data['month'],
                'VP_division_area': data['VP_division_area'],
                'SD_division_area': data['SD_division_area'],
                'VP_blocks_per_zone': data['VP_blocks_per_zone'],
                'SD_blocks_per_zone': data['SD_blocks_per_zone'],
                'VP_zone_size': data['VP_zone_size'],
                'SD_zone_size': data['SD_zone_size'],
                'VP_schemes_per_division': data['VP_schemes_per_division'],
                'SD_schemes_per_division': data['SD_schemes_per_division'],
                'VP_rounds_per_zone': data['VP_rounds_per_zone'],
                'SD_rounds_per_zone': data['SD_rounds_per_zone'],
                'total_pluckers_per_division': data['total_pluckers_per_division'],
                'total_supervisors_per_division': data['total_supervisors_per_division'],
                'total_schemes_per_division': data['total_schemes_per_division'],
            }

            data_object = data.objects.create(**data_dict)
            data_object.save()

            return redirect('/TeaPlucking_planner.html')

    else:
        form = DataForm()

    return render(request, 'TeaPlucking_planner_save_data.html', {'form': form})


def Plucking_requirements(request):
    # create a data frame
    data = {'Zone/Fields': ['ZoneE-12VP', 'ZoneE-5SD', 'ZoneE-3SD', 'ZoneE-15VP', 'ZoneE-7SD', 'ZoneE-14VP',
                            'ZoneF-11SD', 'ZoneF-10SD', 'ZoneF-2VP', 'ZoneF-42VP', 'ZoneF-6SD', 'ZoneF-43VP',
                            'ZoneG-8VP', 'ZoneG-1SD', 'ZoneG-44VP', 'ZoneG-13VP', 'ZoneG-9SD', 'ZoneG-4VP'],
            'Type(VP/SD)': ['VP', 'SD', 'SD', 'VP', 'SD', 'VP',
                            'SD', 'SD', 'VP', 'VP', 'SD', 'VP',
                            'VP', 'SD', 'VP', 'VP', 'SD', 'VP'],
            'Ha.': [12.93, 13.02, 8.27, 10.65, 14.99, 22.60,
                    16.01, 22.55, 7.41, 7.51, 17.00, 4.60,
                    9.07, 17.06, 7.19, 14.34, 20.43, 16.36],
            'Days to Plk': [1, 2, 1, 2, 1, 2,
                            2, 3, 1, 2, 2, 1,
                            1, 2, 1, 2, 2, 2],
            'Prune Age': [2, 2, 1, 0, 3, 4,
                          2, 1, 1, 2, 0, 1,
                          3, 1, 2, 1, 3, 3],
            'Number of Schemes': [185, 145, 92, 152, 167, 323,
                                  178, 251, 106, 107, 189, 66,
                                  130, 190, 103, 205, 227, 234],
            'Growing Days C/F': [1, 2, 1, 2, 1, 'TP',
                                 1, 2, 1, 2, 1, 1,
                                 1, 2, 1, 2, 1, 1]
            }

    df = pd.DataFrame(data, columns=['Zone/Fields', 'Type(VP/SD)', 'Ha.', 'Days to Plk',
                                     'Prune Age', 'Number of Schemes', 'Growing Days C/F'])

    # Calculate the Ha/Day Target
    total_ha = df['Ha.'].sum()
    total_days = df['Days to Plk'].sum()
    ha_day_target = round(total_ha / total_days, 0)

    # Calculate the Pluckers Required
    pluckers_req = 0
    for index, row in df.iterrows():
        if row['Type(VP/SD)'] == 'VP':
            if 700 <= row['Number of Schemes'] <= 900:
                pluckers_req += (row['Number of Schemes'] / 700)
            elif row['Number of Schemes'] > 1200:
                pluckers_req += (row['Number of Schemes'] / 1200)
        else:
            pluckers_req += 0

    # render the HTML template
    return render(request, 'plucking_requirements.html', {'total_ha': total_ha,
                                                          'total_days': total_days,
                                                          'ha_day_target': ha_day_target,
                                                          'pluckers_req': pluckers_req
                                                          })


def PluckingRounds(request):
    today_day = datetime.now()

    fields = [12, 5, 3, 15, 7, 14, 2, 6, 8, 10, 11, 42, 1, 4, 9, 13, 44]

    day = 1

    for field in fields:
        for i in range(31):
            if day <= 8:
                next_plucking = today_day + timedelta(day)
                # print("Pluck field {0} on day {1} next plucking is on{2}".format(field, day, next_plucking))
                day += 1
                if day == 8:
                    break
        else:
            day = 1
            for field in fields:
                next_plucking = today_day + timedelta(day)
                # print("Pluck round {0} on day {1} next plucking is on{2}".format(field, day, next_plucking))
                day += 1
                if day == 8:
                    break
    return render(request, 'pluckingRounds.html')


"""This is a python class 'ProgrammedSchemePlucking' that calculates the plucking capacity and production of tea. The
class has several methods:

init: Initializes all class variables.

set_plucking_input: Prompts the user to input leaf quality, VP and SD percentage, VP and SD division area,
field spacing, maximum bag weight and plucker grade.

calculate_plucking_productivity: Calculates the plucking productivity based on the plucker grade.

calculate_scheme_size: Calculates the size of the plucking scheme.

calculate_zone_size: Calculates the size of a plucking zone.

calculate_plucking_capacity: Calculates the maximum bags of tea produced per day and the total tea production.

display_output: Displays all the calculated values as output."""


def ProgrammedSchemePlucking(request):
    if request.method == 'POST':
        leaf_quality = request.POST['leaf_quality']
        VP_percentage = request.POST['VP_percentage']
        SD_percentage = request.POST['SD_percentage']
        division_area = request.POST['division_area']
        plucker_grade = request.POST['plucker_grade']
        ha = request.POST['ha']
        productivity = request.POST['productivity']
        VP_pluckers_ha = request.POST['VP_pluckers_ha']
        SD_pluckers_ha = request.POST['SD_pluckers_ha']
        zone_number_pluckers = request.POST['zone_number_pluckers']
        VP_scheme = request.POST['VP_scheme']
        SD_scheme = request.POST['SD_scheme']
        obj = ProgrammedSchemePlucking(leaf_quality=leaf_quality,
                                       VP_percentage=VP_percentage,
                                       SD_percentage=SD_percentage,
                                       division_area=division_area,
                                       plucker_grade=plucker_grade,
                                       ha=ha,
                                       productivity=productivity,
                                       VP_pluckers_ha=VP_pluckers_ha,
                                       SD_pluckers_ha=SD_pluckers_ha,
                                       zone_number_pluckers=zone_number_pluckers,
                                       VP_scheme=VP_scheme,
                                       SD_scheme=SD_scheme,
                                       )
        obj.save()
        return render(request, 'ProgrammedSchemePlucking.html', {'obj': obj})
    else:
        return render(request, 'ProgrammedSchemePlucking.html', {})


def plucking_calculation(request):
    if request.method == 'POST':
        obj = ProgrammedSchemePlucking.objects.get(pk=request.POST['obj_id'])
        obj.calculate_plucking_productivity()
        obj.scheme_size()
        obj.calculate_VP_plucking_scheme()
        obj.SD_plucking_scheme()
        obj.zone_size()
        obj.division_size()
        obj.plucking_day_calculations()
        obj.save()
        return render(request, 'ProgrammedSchemePlucking.html', {'obj': obj})
    else:
        return render(request, 'ProgrammedSchemePlucking.html', {})
