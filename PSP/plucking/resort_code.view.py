import csv
from datetime import datetime

# from bs4 import BeautifulSoup
from django.shortcuts import render

from PSP.plucking import models
from PSP.plucking.models import ProgrammedScheme


def PluckingView(request):
    # Define the variable
    datetime.now()
    vp_tea_area = 700  # m^2
    sd_tea_area = 900  # m^2
    pluckers_per_supervisor = 90  # Number of pluckers per supervisor
    schemes_per_day = 2  # Number of schemes per day
    vp_scheme_size = 350  # m^2
    sd_scheme_size = 450  # m^2
    block_size = 2500  # m^2
    vp_plucking_days = 7.5  # Number of days plucking (Plucking Days/Zone)
    sd_plucking_days = 8.5  # Number of days plucking (Plucking Days/Zone)

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

        # working_days_year = 313
        # plucking_rounds_per_year = 36
        # st_round_duration = working_days_year / plucking_rounds_per_year
        vp_round_duration = 7.5
        sd_round_duration = 8.5

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
        data = [
            ['Division Area', division_area],
            ['VP Division Area', vp_division_area],
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
            ['Total Schemes per Division', total_schemes_per_division]
        ]

        with open('data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)

        # Render the HTML page with the data
        context = {
            "data": data
        }
        return render(request, "UpdateFields/plucking_planner_table.html", context)

    # GET request
    else:
        return render(request, "UpdateFields/plucking_planner_table.html")


def PluckingUpdate(request):
    if request.method == 'POST':
        division_area = float(request.POST.get('division_area', '0.00'))
        vp_percentage = float(request.POST.get('VP_percentage', '0.00'))
        sd_percentage = float(request.POST.get('SD_percentage', '0.00'))
        month = request.POST.get('month')
        vp_division_area = float(request.POST.get('VP_division_area', '0.00'))
        sd_division_area = float(request.POST.get('SD_division_area', '0.00'))
        vp_blocks_per_zone = float(request.POST.get('VP_blocks_per_zone', '0.00'))
        sd_blocks_per_zone = float(request.POST.get('SD_blocks_per_zone', '0.00'))
        vp_zone_size = float(request.POST.get('VP_zone_size', '0.00'))
        sd_zone_size = float(request.POST.get('SD_zone_size', '0.00'))
        vp_schemes_per_division = float(request.POST.get('VP_schemes_per_division', '0.00'))
        sd_schemes_per_division = float(request.POST.get('SD_schemes_per_division', '0.00'))
        vp_rounds_per_zone = float(request.POST.get('VP_rounds_per_zone', '0.00'))
        sd_rounds_per_zone = float(request.POST.get('SD_rounds_per_zone', '0.00'))
        total_pluckers_per_division = float(request.POST.get('total_pluckers_per_division', '0.00'))
        total_supervisors_per_division = float(request.POST.get('total_supervisors_per_division', '0.00'))
        total_schemes_per_division = float(request.POST.get('total_schemes_per_division', '0.00'))

        # Perform calculations and generate results based on the form data
        # Replace the following code with your actual logic
        result_data = [
            ('division_area', division_area),
            ('vp_percentage', division_area / vp_division_area * 100),
            ('sd_percentage', division_area / sd_division_area * 100),
            ('month', month),
            ('vp_division_area', sd_percentage * division_area),
            ('sd_division_area', vp_percentage * division_area),
            ('vp_blocks_per_zone', 2500),
            ('sd_blocks_per_zone', 3000),
            ('vp_zone_size', 700),
            ('sd_zone_size', 900),
            ('vp_schemes_per_division', vp_division_area / 350),
            ('sd_schemes_per_division', sd_division_area / 450),
            ('vp_rounds_per_zone', 7.5),
            ('sd_rounds_per_zone', 8.5),
            ('total_pluckers_per_division', division_area / (vp_schemes_per_division + sd_schemes_per_division)),
            ('total_supervisors_per_division', 3),
            ('total_schemes_per_division', division_area / (vp_zone_size + sd_zone_size)),

            # Add more result calculations as needed
        ]

        return render(request, 'UpdateFields/Plucking_planner_update.html', {'data': result_data})

    return render(request, 'UpdateFields/Plucking_planner_update.html')


def ProgrammedSchemeViewRetrieve(request):
    data = ProgrammedScheme.objects.all()
    plucking_date = datetime.now()
    leaf_quality = Decimal(request.GET.get('leaf_quality', 0))
    VP_percentage = Decimal(request.GET.get('VP_percentage', 0))
    SD_percentage = Decimal(request.GET.get('SD_percentage', 0))
    division_area = Decimal(request.GET.get('division_area', 0))
    VP_division_area = (division_area / vp_division_area * 100)
    SD_division_area = (division_area / sd_division_area * 100)

    block_size = ProgrammedScheme.objects.filter('block_size=2500', 0)  # 2500m^2
    VP_scheme = ProgrammedScheme.objects.filter('VP_scheme=700, 0')  # 700m^2
    SD_scheme = ProgrammedScheme.objects.filter('SD_scheme=900, 0')  # 900m^2
    VP_pluckers_ha = (block_size / VP_scheme)  # 2500/700=3.6
    SD_pluckers_ha = (block_size / SD_scheme)  # 2500/900=2.8
    VP_plucked_area_day = (VP_pluckers_ha * block_size)  # VP_pluckers_ha * block_size ha
    SD_plucked_area_day = (SD_pluckers_ha * block_size)  # SD_pluckers_ha * block_size ha
    VP_rounds = ProgrammedScheme.objects.filter('VP_rounds=8, 0')  # 8
    SD_rounds = ProgrammedScheme.objects.filter('SD_rounds=9, 0')  # 9

    vp_zone_size = (vp_rounds * plucked_area_day)  # vp_rounds * plucked_area_day
    sd_zone_size = (sd_rounds * plucked_area_day)  # sd_rounds * plucked_area_day

    VP_zone_number_pluckers = (vp_pluckers_ha * zone_size)  # vp_pluckers_ha * zone_size
    SD_zone_number_pluckers = (sd_pluckers_ha * zone_size)  # sd_pluckers_ha * zone_size
    zone_number_supervisor = ProgrammedScheme.objects.filter('zone_number_supervisor=1, 0')
    total_number_pluckers = ProgrammedScheme.objects.filter(
        VP_zone_number_pluckers + SD_zone_number_pluckers)  # 72ha sd or 50 ha vp 90 per zone,1 supervisor per zone

    context = {
        "ProgrammedScheme": data,
        "plucking_date": plucking_date,
        "leaf_quality": leaf_quality,
        "VP_percentage": VP_percentage,
        "SD_percentage": SD_percentage,
        "division_area": division_area,
        "VP_division_area": VP_division_area,
        "SD_division_area": SD_division_area,
        "block_size": block_size,
        "VP_scheme": VP_scheme,
        "SD_scheme": SD_scheme,
        "VP_pluckers_ha": VP_pluckers_ha,
        "SD_pluckers_ha": SD_pluckers_ha,
        "VP_plucked_area_day": VP_plucked_area_day,
        "SD_plucked_area_day": SD_plucked_area_day,
        "VP_rounds": VP_rounds,
        "SD_rounds": SD_rounds,
        "vp_zone_size": vp_zone_size,
        "sd_zone_size": sd_zone_size,
        "VP_zone_number_pluckers": VP_zone_number_pluckers,
        "SD_zone_number_pluckers": SD_zone_number_pluckers,
        "zone_number_supervisor": zone_number_supervisor,
        "total_number_pluckers": total_number_pluckers,
    }
    return render(request, 'UpdateFields/programmedscheme_record.html', context)


def ProgrammedSchemeViewUpdate(request):
    VP_division_area = (division_area / vp_division_area * 100)
    if VP_division_area is None:
        VP_division_area = 0
    else:
        VP_division_area = (division_area / vp_division_area * 100)
    SD_division_area = (division_area / sd_division_area * 100)
    if SD_division_area is None:
        SD_division_area = 0
    else:
        SD_division_area = (division_area / sd_division_area * 100)
    VP_pluckers_ha = (block_size / VP_scheme)
    if VP_pluckers_ha is None:
        VP_pluckers_ha = 0
    else:
        VP_pluckers_ha = (block_size / VP_scheme)
    SD_pluckers_ha = (block_size / SD_scheme)
    if SD_pluckers_ha is None:
        SD_pluckers_ha = 0
    else:
        SD_pluckers_ha = (block_size / SD_scheme)
    VP_plucked_area_day = (VP_pluckers_ha * block_size)
    if VP_plucked_area_day is None:
        VP_plucked_area_day = 0
    else:
        VP_plucked_area_day = (VP_pluckers_ha * block_size)

    SD_plucked_area_day = (SD_pluckers_ha * block_size)
    if SD_plucked_area_day is None:
        SD_plucked_area_day = 0
    else:
        SD_plucked_area_day = (SD_pluckers_ha * block_size)

    vp_zone_size = (vp_rounds * plucked_area_day)
    if vp_zone_size is None:
        vp_zone_size = 0
    else:
        vp_zone_size = (vp_rounds * plucked_area_day)

    sd_zone_size = (sd_rounds * plucked_area_day)
    if sd_zone_size is None:
        sd_zone_size = 0
    else:
        sd_zone_size = (sd_rounds * plucked_area_day)

    VP_zone_number_pluckers = (vp_pluckers_ha * zone_size)
    if VP_zone_number_pluckers is None:
        VP_zone_number_pluckers = 0
    else:
        VP_zone_number_pluckers = (vp_pluckers_ha * zone_size)

    SD_zone_number_pluckers = (sd_pluckers_ha * zone_size)
    if SD_zone_number_pluckers is None:
        SD_zone_number_pluckers = 0
    else:
        SD_zone_number_pluckers = (sd_pluckers_ha * zone_size)

    total_number_pluckers = ProgrammedScheme.objects.filter(VP_zone_number_pluckers + SD_zone_number_pluckers)
    if total_number_pluckers is None:
        total_number_pluckers = 0
    else:
        total_number_pluckers = ProgrammedScheme.objects.filter(VP_zone_number_pluckers + SD_zone_number_pluckers)

    context = {
        "VP_division_area": VP_division_area,
        "SD_division_area": SD_division_area,
        "VP_pluckers_ha": VP_pluckers_ha,
        "SD_pluckers_ha": SD_pluckers_ha,
        "VP_plucked_area_day": VP_plucked_area_day,
        "SD_plucked_area_day": SD_plucked_area_day,
        "vp_zone_size": vp_zone_size,
        "sd_zone_size": sd_zone_size,
        "VP_zone_number_pluckers": VP_zone_number_pluckers,
        "SD_zone_number_pluckers": SD_zone_number_pluckers,
        "total_number_pluckers": total_number_pluckers,
    }
    return render(request, 'UpdateFields/programmedscheme_update.html', context)


def ProgrammedSchemeViewCreate(request):
    if request.method == "POST":
        plucking_date = request.POST['plucking_date']
        leaf_quality = request.POST['leaf_quality']
        VP_percentage = request.POST['VP_percentage']
        SD_percentage = request.POST['SD_percentage']
        division_area = request.POST['division_area']
        VP_division_area = request.POST['VP_division_area']
        SD_division_area = request.POST['SD_division_area']
        block_size = request.POST['block_size']
        VP_scheme = request.POST['VP_scheme']
        SD_scheme = request.POST['SD_scheme']
        VP_pluckers_ha = request.POST['VP_pluckers_ha']
        SD_pluckers_ha = request.POST['SD_pluckers_ha']
        VP_plucked_area_day = request.POST['VP_plucked_area_day']
        SD_plucked_area_day = request.POST['SD_plucked_area_day']
        VP_rounds = request.POST['VP_rounds']
        SD_rounds = request.POST['SD_rounds']
        vp_zone_size = request.POST['vp_zone_size']
        sd_zone_size = request.POST['sd_zone_size']
        VP_zone_number_pluckers = request.POST['VP_zone_number_pluckers']
        SD_zone_number_pluckers = request.POST['SD_zone_number_pluckers']
        zone_number_supervisor = request.POST['zone_number_supervisor']
        total_number_pluckers = request.POST['total_number_pluckers']

        insert = programmedScheme(plucking_date=plucking_date, leaf_quality=leaf_quality, VP_percentage=VP_percentage,
                                  SD_percentage=SD_percentage, division_area=division_area,
                                  VP_division_area=VP_division_area, SD_division_area=SD_division_area,
                                  block_size=block_size, VP_scheme=VP_scheme,
                                  SD_scheme=SD_scheme, VP_pluckers_ha=VP_pluckers_ha,
                                  SD_pluckers_ha=SD_pluckers_ha, VP_plucked_area_day=VP_plucked_area_day,
                                  SD_plucked_area_day=SD_plucked_area_day, VP_rounds=VP_rounds,
                                  SD_rounds=SD_rounds, vp_zone_size=vp_zone_size,
                                  sd_zone_size=sd_zone_size, VP_zone_number_pluckers=VP_zone_number_pluckers,
                                  SD_zone_number_pluckers=SD_zone_number_pluckers,
                                  zone_number_supervisor=zone_number_supervisor,
                                  total_number_pluckers=total_number_pluckers)

        insert.save()
        return redirect('/programmedScheme-record')
