from datetime import datetime, timedelta
from decimal import Decimal

import pandas as pd
from django.db.models import Sum
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

from . import models
from .forms import ProgrammedSchemeForm, PSPForms, RoundsMonitorForm
from .models import ProgrammedScheme, RoundsMonitor, DataEntry
from django.db.models import IntegerField



def Resourcesexcell(request):
    pass
    return HttpResponse('127.0.0.1:8000/Resourcesexcell-admin/')


def Admin(request):
    pass
    return HttpResponse('admin/')


def AdminResources(request):
    pass

    return HttpResponse('This is the plucking reports Page')


def PSP(request):
    context = {
        'name': {'This is the plucking reports Page'},
        'form': PSPForms
    }
    return render(request, 'UpdateFields/psp.html', context)


def PSPGraphs(request):
    context = {
        'name': {'This is the plucking graphs dashboard'},
        'form': PSPForms
    }
    return render(request, 'UpdateFields/psp_graphs.html', context)


def FirstPage(request):
    context = {
        'name': {'This is the plucking graphs dashboard'},
        'form': PSPForms
    }
    return render(request, 'UpdateFields/psp_graphs_board.html', context)


def PSPCalculator(request):
    context = {
        'name': {'This is the plucking reports Page'},
        'form': PSPForms
    }
    return render(request, 'UpdateFields/test.html', {'context': context})


########################################################################################################################
def RoundsMonitorViewRetrieve(request):
    data = RoundsMonitor.objects.all()
    current_date = datetime.strptime("2023-05-01T20:16", "%Y-%m-%dT%H:%M")
    field = IntegerField()
    today_date = datetime.strptime("2023-05-01T20:16", "%Y-%m-%dT%H:%M")
    plucking_round = 8
    plucking_day = datetime.now()
    timestamp = int(plucking_day.timestamp())
    plucking_day = today_date + timedelta(days=plucking_round)
    next_plucking = timestamp + plucking_round
    actual_plucking_day = int(current_date.strftime("%Y%m%d")) + plucking_round

    total_plucking_round = RoundsMonitor.objects.aggregate(Sum('plucking_round'))['plucking_round__sum']
    if total_plucking_round is None:
        total_plucking_round = 0

    month_end = today_date.replace(day=1, month=today_date.month + 1) - timedelta(days=1)
    if today_date.month == 2:
        if today_date.year % 4 == 0 and (today_date.year % 100 != 0 or today_date.year % 400 == 0):
            month_end = month_end.replace(day=29)
        else:
            month_end = month_end.replace(day=28)
    elif today_date.month in [1, 3, 5, 7, 8, 10, 12]:
        month_end = month_end.replace(day=31)
    else:
        month_end = month_end.replace(day=30)
    round_bal_days = month_end.day - total_plucking_round
    days_to_end_month = month_end.day - round_bal_days
    days_bf = days_to_end_month - round_bal_days

    context = {
        "roundsmonitor": data,
        "field": field,
        "today_date": today_date,
        "plucking_round": plucking_round,
        "plucking_day": plucking_day,
        "next_plucking": next_plucking,
        "actual_plucking_day": actual_plucking_day,
        "total_plucking_round": total_plucking_round,
        "month_end": month_end,
        "round_bal_days": round_bal_days,
        "days_to_end_month": days_to_end_month,
        "days_bf": days_bf,
    }
    return render(request, 'UpdateFields/rounds_monitor.html', context)


def RoundsMonitorViewUpdate(request):

    current_date = datetime.strptime("2023-05-01T20:16", "%Y-%m-%dT%H:%M")
    plucking_round = 8
    if plucking_round is None:
        plucking_round = 0
    else:
        plucking_round = int(plucking_round)
    plucking_day = datetime.now()
    timestamp = int(plucking_day.timestamp())
    plucking_day = current_date + timedelta(days=plucking_round)
    next_plucking = timestamp + plucking_round
    actual_plucking_day = int(current_date.strftime("%Y%m%d")) + plucking_round
    days_behind = timestamp - actual_plucking_day
    if isinstance(days_behind, timedelta):
        days_behind = days_behind.days
    else:
        days_behind = 0
    # Use days property to get the difference in days
    days_ahead = (current_date + timedelta(days=plucking_round) - current_date).days
    total_plucking_round = RoundsMonitor.objects.aggregate(Sum('plucking_round'))['plucking_round__sum']
    if total_plucking_round is None:
        total_plucking_round = 0
    else:
        total_plucking_round = int(total_plucking_round)
    month_end = current_date.replace(day=1, month=current_date.month + 1).replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)
    if current_date.month == 2:
        if current_date.year % 4 == 0 and (current_date.year % 100 != 0 or current_date.year % 400 == 0):
            month_end = month_end.replace(day=29)
        else:
            month_end = month_end.replace(day=28)
    elif current_date.month in [1, 3, 5, 7, 8, 10, 12]:
        month_end = month_end.replace(day=31)
    else:
        month_end = month_end.replace(day=30)
    round_bal_days = month_end.day - total_plucking_round
    days_to_end_month = month_end.day - round_bal_days
    days_bf = days_to_end_month - round_bal_days

    context = {

        "current_date": current_date,
        "plucking_round": plucking_round,
        "plucking_day": plucking_day,
        "next_plucking": next_plucking,
        "actual_plucking_day": actual_plucking_day,
        "days_behind": days_behind,  # Use days property to get the difference in days
        "days_ahead": days_ahead,
        "total_plucking_round": total_plucking_round,
        "month_end": month_end.day,  # Store only the day of the month
        "round_bal_days": round_bal_days,
        "days_to_end_month": days_to_end_month,
        "days_bf": days_bf,
    }

    # Save the record
    # data.month_end = month_end.day
    # data.save()

    return render(request, 'UpdateFields/rounds_monitor_update.html', context)


def RoundsMonitoViewCreate(request):
    if request.method == "POST":
        today_date = request.GET.get('today_date') or None
        field = request.POST['field']
        plucking_round = request.POST['plucking_round']
        plucking_day = request.GET.get('plucking_day') or None
        next_plucking = request.GET.get('next_plucking') or None
        actual_plucking_day = request.GET.get('actual_plucking_day') or None
        days_behind = request.POST['days_behind']
        days_ahead = request.POST['days_ahead']
        total_plucking_round = request.POST['total_plucking_round']
        month_end = request.POST['month_end']
        round_bal_days = request.POST['round_bal_days']
        days_to_end_month = request.POST['days_to_end_month']
        days_bf = request.POST['days_bf']

        insert = RoundsMonitor(today_date=today_date,field=field, plucking_round=plucking_round, plucking_day=plucking_day,
                               next_plucking=next_plucking, actual_plucking_day=actual_plucking_day,
                               days_behind=days_behind, days_ahead=days_ahead,
                               total_plucking_round=total_plucking_round, month_end=month_end,
                               round_bal_days=round_bal_days, days_to_end_month=days_to_end_month,
                               days_bf=days_bf, )

        insert.save()
        return redirect('/roundsmonitor-record')


def chart_view(request):
    data = DataEntry.objects.all()
    # Retrieve your table data from the database or any other source
    table_data = [
        {'plucking_date': '2023-01-01', 'leaf_quality': 10},
        {'plucking_date': '2023-01-02', 'leaf_quality': 15},
        {'plucking_date': '2023-01-03', 'leaf_quality': 8},
        # Add more entries as needed
    ]
    # Prepare the chart data
    chart_data = [{'plucking_date': entry['plucking_date'], 'leaf_quality': entry['leaf_quality']} for entry in
                  table_data]

    context = {
        'chart_data': chart_data
    }
    return render(request, 'UpdateFields/psp_graphs_board.html', context)


########################################################################################################################
def ProgrammedSchemeViewRetrieve(request):
    data = ProgrammedScheme.objects.all()
    plucking_date = datetime.strptime("2023-05-01T20:16", "%Y-%m-%dT%H:%M")
    leaf_quality = Decimal(request.GET.get('leaf_quality', 0))
    VP_percentage = Decimal(request.GET.get('VP_percentage', 0))
    SD_percentage = Decimal(request.GET.get('SD_percentage', 0))
    division_area = Decimal(request.GET.get('division_area', 0))
    VP_division_area = (Decimal(request.GET.get('VP_division_area', 0)))
    SD_division_area = (Decimal(request.GET.get('SD_division_area', 0)))
    block_size = 2500
    VP_scheme = 700
    SD_scheme = 900
    VP_pluckers_ha = 3.6
    SD_pluckers_ha = 2.8
    VP_plucked_area_day = VP_pluckers_ha * block_size
    SD_plucked_area_day = SD_pluckers_ha * block_size
    VP_rounds = 8
    SD_rounds = 9
    VP_zone_size = VP_rounds * 6.25
    SD_zone_size = SD_rounds * 8
    VP_zone_number_pluckers = VP_pluckers_ha * VP_zone_size
    SD_zone_number_pluckers = SD_pluckers_ha * SD_zone_size
    zone_number_supervisor = 1
    total_number_pluckers = VP_zone_number_pluckers + SD_zone_number_pluckers

    context = {
        "programmedScheme": data,
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
        "VP_zone_size": VP_zone_size,
        "SD_zone_size": SD_zone_size,
        "VP_zone_number_pluckers": VP_zone_number_pluckers,
        "SD_zone_number_pluckers": SD_zone_number_pluckers,
        "zone_number_supervisor": zone_number_supervisor,
        "total_number_pluckers": total_number_pluckers,
    }
    return render(request, 'UpdateFields/programmedscheme_record.html', context)


def ProgrammedSchemeViewUpdate(request):
    division_area = 242
    VP_percentage = 39
    SD_percentage = 61
    block_size = 2500
    VP_scheme = 700
    SD_scheme = 900
    VP_pluckers_ha = 3.6
    SD_pluckers_ha = 2.8
    VP_rounds = 8
    SD_rounds = 9
    VP_zone_size = 50
    SD_zone_size = 72
    VP_division_area = division_area / 100 * VP_percentage
    SD_division_area = division_area / 100 * SD_percentage
    VP_plucked_area_day = VP_pluckers_ha * block_size
    SD_plucked_area_day = SD_pluckers_ha * block_size
    VP_zone_number_pluckers = VP_pluckers_ha * VP_zone_size
    SD_zone_number_pluckers = SD_pluckers_ha * SD_zone_size
    zone_number_supervisor = 1
    total_number_pluckers = VP_zone_number_pluckers + SD_zone_number_pluckers

    context = {
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
        "VP_zone_size": VP_zone_size,
        "SD_zone_size": SD_zone_size,
        "VP_zone_number_pluckers": VP_zone_number_pluckers,
        "SD_zone_number_pluckers": SD_zone_number_pluckers,
        "zone_number_supervisor": zone_number_supervisor,
        "total_number_pluckers": total_number_pluckers,
    }

    return render(request, 'UpdateFields/programmedscheme_update.html', context)


def ProgrammedSchemeViewCreate(request):
    if request.method == "POST":
        plucking_date = request.GET.get('plucking_date') or None
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
        VP_zone_size = request.POST['VP_zone_size']
        SD_zone_size = request.POST['SD_zone_size']
        VP_zone_number_pluckers = request.POST['VP_zone_number_pluckers']
        SD_zone_number_pluckers = request.POST['SD_zone_number_pluckers']
        zone_number_supervisor = request.POST['zone_number_supervisor']
        total_number_pluckers = request.POST['total_number_pluckers']

        insert = ProgrammedScheme(plucking_date=plucking_date, leaf_quality=leaf_quality, VP_percentage=VP_percentage,
                                  SD_percentage=SD_percentage, division_area=division_area,
                                  VP_division_area=VP_division_area, SD_division_area=SD_division_area,
                                  block_size=block_size, VP_scheme=VP_scheme,
                                  SD_scheme=SD_scheme, VP_pluckers_ha=VP_pluckers_ha,
                                  SD_pluckers_ha=SD_pluckers_ha, VP_plucked_area_day=VP_plucked_area_day,
                                  SD_plucked_area_day=SD_plucked_area_day, VP_rounds=VP_rounds,
                                  SD_rounds=SD_rounds, VP_zone_size=VP_zone_size,
                                  SD_zone_size=SD_zone_size, VP_zone_number_pluckers=VP_zone_number_pluckers,
                                  SD_zone_number_pluckers=SD_zone_number_pluckers,
                                  zone_number_supervisor=zone_number_supervisor,
                                  total_number_pluckers=total_number_pluckers)

        insert.save()
        return redirect('/programmedscheme-record')


########################################################################################################################

def ProgrammedSchemeUpdate(request, pk):
    programmedScheme = ProgrammedScheme.objects.get(id=pk)
    if request.method == 'POST':
        form = ProgrammedSchemeForm(request.POST, instance=programmedScheme)
        if form.is_valid():
            form.save()
            return redirect('/programmedscheme-record')

    else:
        form = ProgrammedSchemeForm(instance=programmedScheme)

    context = {
        'form': form, 'UpdatePluckingForm': ProgrammedSchemeForm,

    }
    return render(request, 'ProgrammedScheme/update.html', context)


def ProgrammedSchemeDelete(request, pk):
    data = ProgrammedScheme.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('/programmedscheme-record')

    context = {
        'data': data,
    }
    return render(request, 'ProgrammedScheme/delete.html', context)


def save_changes(request):
    row_index = request.POST.get('rowIndex')
    cell_index = request.POST.get('cellIndex')
    cell_value = request.POST.get('cellValue')

    # Process and save the cell changes
    # Here, you can store the data in a database or any other storage mechanism

    return JsonResponse({'status': 'success'})


def RoundsMonitorEdit(request, pk):
    roundsmonitor = RoundsMonitor.objects.get(id=pk)
    if request.method == 'POST':
        form = RoundsMonitorForm(request.POST, instance=roundsmonitor)
        if form.is_valid():
            form.save()
            return redirect('/roundsmonitor-record')

    else:
        form = RoundsMonitorForm(instance=roundsmonitor)

    context = {
        'form': form, 'RoundsMonitorForm': RoundsMonitorForm,

    }
    return render(request, 'RoundsMonitor/update.html', context)


def RoundsMonitorDelete(request, pk):
    data = RoundsMonitor.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('/roundsmonitor-record')

    context = {
        'data': data,
    }
    return render(request, 'RoundsMonitor/delete.html', context)


########################################################################################################################
def PluckingRoundsViewRetrieve(request):
    table = {
        'Zone E': {
            'Field': ['5', '3', '7', '12', '14', '15'],
            'Leaf_Type': ['SD', 'SD', 'VP', 'VP', 'VP'],
            'Ha': [13.02, 8.27, 14.99, 12.93, 22.60, 10.65],
            'Days_to_Plk': [1, 2, 1, 2, 2, 1],
            'Prune_Age': [2, 2, 1, 0, 3, 4],
            'Num_of_Schemes': [185, 145, 92, 152, 323, 167],
            'Growing_Days_C/f': [1, 2, 1, 2, 1, 0]
        },
        'Zone F': {
            'Field': ['11', '10', '42', '2', '6', '43'],
            'Leaf_Type': ['SD', 'SD', 'VP', 'SD', 'VP'],
            'Ha': [16.01, 22.55, 7.51, 7.41, 17.00, 4.6],
            'Days_to_Plk': [2, 3, 1, 1, 2, 1],
            'Prune_Age': [2, 1, 3, 1, 0, 1],
            'Num_of_Schemes': [178, 251, 107, 106, 189, 66],
            'Growing_Days_C/f': [9, 3, 1, 3, 1, 2]
        },
        'Zone G': {
            'Field': ['8', '1', '44', '13', '9', '4'],
            'Leaf_Type': ['VP', 'SD', 'VP', 'VP', 'SD', 'VP'],
            'Ha': [9.07, 17.06, 7.19, 14.34, 20.43, 16.36],
            'Days_to_Plk': [1, 2, 1, 1, 2, 2],
            'Prune_Age': [3, 1, 2, 1, 3, 3],
            'Num_of_Schemes': [130, 190, 103, 205, 227, 234],
            'Growing_Days_C/f': [7, 7, 3, 2, 1, 0]
        }
    }

    if request.method == 'POST':
        zone = request.POST.get('zone')
        key = request.POST.get('key')
        index = request.POST.get('index')
        new_value = request.POST.get('new_value')

        if zone in table and key in table[zone] and index is not None:
            index = int(index)
            table[zone][key][index] = new_value

    # Generate the HTML table dynamically from the table dictionary
    html = "<table>"

    # Iterate over the zones in the table dictionary
    for zone, data in table.items():
        html += "<tr>"
        html += f"<td>{zone}</td>"

        # Iterate over the keys and values in the zone's data dictionary
        for key, values in data.items():
            html += "<td>"
            html += key
            html += "</td>"

            # Iterate over the values in the current key
            for index, value in enumerate(values):
                html += "<td>"
                html += f'<input type="text" name="zone={zone}&key={key}&index={index}" value="{value}" />'
                html += "</td>"

        html += "</tr>"

    html += "</table>"

    context = {
        'html': html,
    }

    return render(request, 'UpdateFields/pluckingRounds.html', context)


def PluckingRoundsViewUpdate(request):
    table = {
        'Zone E': {
            'Field': ['5', '3', '7', '12', '14', '15'],
            'Leaf_Type': ['SD', 'SD', 'VP', 'VP', 'VP'],
            'Ha': [13.02, 8.27, 14.99, 12.93, 22.60, 10.65],
            'Days_to_Plk': [1, 2, 1, 2, 2, 1],
            'Prune_Age': [2, 2, 1, 0, 3, 4],
            'Num_of_Schemes': [185, 145, 92, 152, 323, 167],
            'Growing_Days_C/f': [1, 2, 1, 2, 1, 0]
        },
        'Zone F': {
            'Field': ['11', '10', '42', '2', '6', '43'],
            'Leaf_Type': ['SD', 'SD', 'VP', 'SD', 'VP'],
            'Ha': [16.01, 22.55, 7.51, 7.41, 17.00, 4.6],
            'Days_to_Plk': [2, 3, 1, 1, 2, 1],
            'Prune_Age': [2, 1, 3, 1, 0, 1],
            'Num_of_Schemes': [178, 251, 107, 106, 189, 66],
            'Growing_Days_C/f': [9, 3, 1, 3, 1, 2]
        },
        'Zone G': {
            'Field': ['8', '1', '44', '13', '9', '4'],
            'Leaf_Type': ['VP', 'SD', 'VP', 'VP', 'SD', 'VP'],
            'Ha': [9.07, 17.06, 7.19, 14.34, 20.43, 16.36],
            'Days_to_Plk': [1, 2, 1, 1, 2, 2],
            'Prune_Age': [3, 1, 2, 1, 3, 3],
            'Num_of_Schemes': [130, 190, 103, 205, 227, 234],
            'Growing_Days_C/f': [7, 7, 3, 2, 1, 0]
        }
    }

    if request.method == 'POST':
        # Get the zone, key, and index to update from the form data
        zone = request.POST.get('zone')
        key = request.POST.get('key')
        index = request.POST.get('index')
        # Get the new value to set in the cell
        new_value = request.POST.get('new_value')
        # Update the value in the table
        if index is not None:
            index = int(index)
            table[zone][key][index] = new_value

    # Generate the HTML table dynamically from the table dictionary
    html = "<table>"

    # Iterate over the zones in the table dictionary
    for zone, data in table.items():
        html += "<tr>"
        html += f"<td>{zone}</td>"
        # Iterate over the keys and values in the zone's data dictionary
        for key, values in data.items():
            html += "<td>"
            html += f"{key}</td>"

            # Iterate over the values in the current key's list
            for index, value in enumerate(values):
                html += "<td>"
                if value:
                    html += str(value)
                else:
                    # Generate an input field
                    html += f'<input type="text" name="zone_{zone}_{key}_{index}" value="{value}"/>'
                html += "</td>"

        html += "</tr>"

    html += "</table>"

    context = {
        'html_table': html,
    }

    return render(request, 'UpdateFields/pluckingRoundsUpdate.html', context)


def PluckingRoundsViewCreate(request):
    if request.method == "POST":
        table = request.POST['table']
        table.save()

    return render(request, 'UpdateFields/pluckingRounds.html')


def ZoneFieldsViewRetrieve(request, df=None):
    data = {'Zone_field': ['ZoneE-12VP', 'ZoneE-5SD', 'ZoneE-3SD', 'ZoneE-15VP', 'ZoneE-7SD', 'ZoneE-14VP',
                           'ZoneF-11SD', 'ZoneF-10SD', 'ZoneF-2VP', 'ZoneF-42VP', 'ZoneF-6SD', 'ZoneF-43VP',
                           'ZoneG-8VP', 'ZoneG-1SD', 'ZoneG-44VP', 'ZoneG-13VP', 'ZoneG-9SD', 'ZoneG-4VP'],
            'Leaf_type(VP/SD)': ['VP', 'SD', 'SD', 'VP', 'SD', 'VP',
                                 'SD', 'SD', 'VP', 'VP', 'SD', 'VP',
                                 'VP', 'SD', 'VP', 'VP', 'SD', 'VP'],
            'Ha.': [12.93, 13.02, 8.27, 10.65, 14.99, 22.60,
                    16.01, 22.55, 7.41, 7.51, 17.00, 4.60,
                    9.07, 17.06, 7.19, 14.34, 20.43, 16.36],
            'Days_to_plk': [1, 2, 1, 2, 1, 2,
                            2, 3, 1, 2, 2, 1,
                            1, 2, 1, 2, 2, 2],
            'Prune_age': [2, 2, 1, 0, 3, 4,
                          2, 1, 1, 2, 0, 1,
                          3, 1, 2, 1, 3, 3],
            'Number_of_schemes': [185, 145, 92, 152, 167, 323,
                                  178, 251, 106, 107, 189, 66,
                                  130, 190, 103, 205, 227, 234],
            'Growing_days_CF': [1, 2, 1, 2, 1, 0,
                                1, 2, 1, 2, 1, 1,
                                1, 2, 1, 2, 1, 1]
            }

    df = pd.DataFrame(data, columns=['Zone_field', 'Leaf_type(VP/SD)', 'Ha.', 'Days_to_plk',
                                     'Prune_age', 'Number_of_schemes', 'Growing_days_CF'])

    context = {'data': df}
    return render(request, 'UpdateFields/zone_fields.html', context)


def ZoneFieldsViewUpdate(request):
    data = Fields.objects.all()

    context = {
        "data": data,
    }
    return render(request, 'UpdateFields/update_zone_fields.html', context)


def save_edited_content(request):
    if request.method == 'POST' and request.is_ajax():
        edited_content = request.POST.get('content')
        request.session['editableCellContent'] = edited_content
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

########################################################################################################################
