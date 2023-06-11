import decimal
from calendar import month
from datetime import datetime, timedelta
from decimal import Decimal, InvalidOperation

import day
import pandas as pd
from django.db.models import Sum, Count
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from django.db import models

from . import models
from .forms import ProgrammedSchemeForm, PSPForms, RoundsMonitorForm, FieldsForm, FieldsForms, CycleForms
from .models import ProgrammedScheme, RoundsMonitor, DataEntry, FieldsToPluck, AutoFields, TeaPluckingCycle
from django.db.models import IntegerField
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import AutoFields


def Resourcesexcell(request):
    pass
    return HttpResponse('127.0.0.1:8000/Resourcesexcell-admin/')


def FirstPage(request):
    context = {
        'name': {'welcome to the first Page'},
        'form': PSPForms
    }
    return render(request, 'Plucking/first_page.html', context)


def PSPDashboard(request):
    context = {
        'name': {'This is the plucking reports Page'},
        'form': PSPForms
    }
    return render(request, 'Plucking/dasboard.html', context)


def PSPGraphs(request):
    context = {
        'name': {'This is the plucking graphs dashboard'},
        'form': PSPForms
    }
    return render(request, 'Plucking/graphs_psp.html', context)


def RoundsMonitorViewRetrieve(request):
    data = RoundsMonitor.objects.all()
    current_date = datetime.strptime("2023-05-01T20:16", "%Y-%m-%dT%H:%M")
    field = IntegerField()
    rd_today_date = datetime.strptime("2023-05-01T20:16", "%Y-%m-%dT%H:%M")  # round_today_date
    plucking_round = 8
    plucking_day = datetime.now()
    if plucking_day:
        timestamp = int(plucking_day.timestamp())
    else:
        # Handle the case when Plucking_day is None or invalid
        timestamp = 0
    next_plucking = int(timestamp + plucking_round)
    actual_plucking_day = int(current_date.strftime("%Y%m%d")) + plucking_round
    days_behind = int(timestamp - actual_plucking_day)
    days_ahead = (current_date + timedelta(days=plucking_round) - current_date).days
    total_plucking_round = RoundsMonitor.objects.aggregate(Count('plucking_round'))['plucking_round__count']
    if total_plucking_round is None:
        total_plucking_round = 0
    month_end = rd_today_date.replace(day=1, month=rd_today_date.month + 1) - timedelta(days=1)
    if rd_today_date.month == 2:
        if rd_today_date.year % 4 == 0 and (rd_today_date.year % 100 != 0 or rd_today_date.year % 400 == 0):
            month_end = month_end.replace(day=29)
        else:
            month_end = month_end.replace(day=28)
    elif rd_today_date.month in [1, 3, 5, 7, 8, 10, 12]:
        month_end = month_end.replace(day=31)
    else:
        month_end = month_end.replace(day=30)
    round_bal_days = month_end.day - (total_plucking_round * 8)
    if round_bal_days <= month_end.day:
        round_bal_days = 0
    else:
        round_bal_days = month_end.day - (total_plucking_round * 8)
    today_date = datetime.today().date()
    n = month_end.date() - today_date
    months = int(n.days / 30)
    days_to_end_month = month_end.day - (total_plucking_round * 8)
    if days_to_end_month <= 0:
        days_to_end_month = 0
    days_bf = (month_end.day - (total_plucking_round * 8))
    if days_bf >= 0:
        if (total_plucking_round * 8) >= 8 or 16 or 24:
            days_bf = days_bf % 8

    context = {
        "roundsmonitor": data,
        "field": field,
        "rd_today_date": today_date,
        "plucking_round": plucking_round,
        "Plucking_day": plucking_day,
        "next_plucking": next_plucking,
        "actual_plucking_day": actual_plucking_day,
        "days_behind": days_behind,
        "days_ahead": days_ahead,
        "total_plucking_round": total_plucking_round,
        "month_end": month_end,
        "round_bal_days": round_bal_days,
        "days_to_end_month": days_to_end_month,
        "days_bf": days_bf,
    }
    return render(request, 'Plucking/rounds_monitor.html', context)


def RoundsMonitorViewUpdate(request):
    current_date = datetime.strptime("2023-05-01T20:16", "%Y-%m-%dT%H:%M")
    plucking_round = 8
    if plucking_round is None:
        plucking_round = 0
    else:
        plucking_round = int(plucking_round)
    plucking_day = datetime.now()
    if plucking_day:
        timestamp = int(plucking_day.timestamp())
    else:
        # Handle the case when Plucking_day is None or invalid
        timestamp = 0

    next_plucking = int(timestamp + plucking_round)
    if next_plucking is None:
        next_plucking = 0
    else:
        next_plucking = int(timestamp + plucking_round)
    actual_plucking_day = int(current_date.strftime("%Y%m%d")) + plucking_round
    if actual_plucking_day is None:
        actual_plucking_day = 0
    else:
        actual_plucking_day = int(current_date.strftime("%Y%m%d")) + plucking_round
    days_behind = int(timestamp - actual_plucking_day)
    if isinstance(days_behind, timedelta):
        days_behind = days_behind.days
    else:
        days_behind = 0
    # Use days property to get the difference in days
    days_ahead = (current_date + timedelta(days=plucking_round) - current_date).days
    total_plucking_round = RoundsMonitor.objects.aggregate(Count('plucking_round'))['plucking_round__count']
    if total_plucking_round is None:
        total_plucking_round = 0
    else:
        total_plucking_round = int(total_plucking_round)
    month_end = current_date.replace(day=1, month=current_date.month + 1).replace(hour=0, minute=0, second=0,
                                                                                  microsecond=0) - timedelta(days=1)
    if current_date.month == 2:
        if current_date.year % 4 == 0 and (current_date.year % 100 != 0 or current_date.year % 400 == 0):
            month_end = month_end.replace(day=29)
        else:
            month_end = month_end.replace(day=28)
    elif current_date.month in [1, 3, 5, 7, 8, 10, 12]:
        month_end = month_end.replace(day=31)
    else:
        month_end = month_end.replace(day=30)
    round_bal_days = month_end.day - (total_plucking_round * 8)
    if round_bal_days == month_end:
        round_bal_days = 0
    else:
        round_bal_days = month_end.day - (total_plucking_round * 8)
    today_date = datetime.today().date()
    n = month_end.date() - today_date
    months = int(n.days / 30)
    days_to_end_month = round_bal_days + 8 - month_end.day
    if days_to_end_month <= 0:
        days_to_end_month = 0
    days_bf = months - round_bal_days
    if days_bf <= 0:
        days_bf = 0

    context = {

        "current_date": current_date,
        "plucking_round": plucking_round,
        "Plucking_day": plucking_day,
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

    return render(request, 'Plucking/rounds_monitor_update.html', context)


def RoundsMonitoViewCreate(request):
    if request.method == "POST":
        today_date = request.GET.get('today_date') or None
        field = request.POST['field']
        plucking_round = request.POST['plucking_round']
        plucking_day = request.GET.get('Plucking_day') or None
        next_plucking = request.GET.get('next_plucking') or None
        actual_plucking_day = request.GET.get('actual_plucking_day') or None
        days_behind = request.POST['days_behind']
        days_ahead = request.POST['days_ahead']
        total_plucking_round = request.POST['total_plucking_round']
        month_end = request.POST['month_end']
        round_bal_days = request.POST['round_bal_days']
        days_to_end_month = request.POST['days_to_end_month']
        days_bf = request.POST['days_bf']

        insert = RoundsMonitor(today_date=today_date, field=field, plucking_round=plucking_round,
                               plucking_day=plucking_day,
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
    return render(request, 'Plucking/psp_graphs_board.html', context)


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
    return render(request, 'Plucking/programmedscheme_record.html', context)


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

    return render(request, 'Plucking/programmedscheme_update.html', context)


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
        'form': form,
        'UpdatePluckingForm': ProgrammedSchemeForm,

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
    # Example: Saving the changes in a database using Django's models and ORM
    # Replace MyModel with your actual model name

    # Retrieve the row or create a new row if it doesn't exist
    row, created = RoundsMonitor.objects.get_or_create(index=row_index)

    # Update the cell value for the given cell index in the row
    row.cells[cell_index] = cell_value

    # Save the updated row
    row.save()

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


def PluckingRoundsViewRetrieve(request):
    table = {
        'Zone E': {
            'Field': ['5', '3', '7', '12', '14', '15'],
            'Leaf_Type': ['SD', 'SD', 'VP', 'VP', 'VP'],
            'Ha': [13.02, 8.27, 14.99, 12.93, 22.60, 10.65],
            'Days_to_plk': [1, 2, 1, 2, 2, 1],
            'Prune_age': [2, 2, 1, 0, 3, 4],
            'Num_of_Schemes': [185, 145, 92, 152, 323, 167],
            'Growing_Days_C/f': [1, 2, 1, 2, 1, 0]
        },
        'Zone F': {
            'Field': ['11', '10', '42', '2', '6', '43'],
            'Leaf_Type': ['SD', 'SD', 'VP', 'SD', 'VP'],
            'Ha': [16.01, 22.55, 7.51, 7.41, 17.00, 4.6],
            'Days_to_plk': [2, 3, 1, 1, 2, 1],
            'Prune_age': [2, 1, 3, 1, 0, 1],
            'Num_of_Schemes': [178, 251, 107, 106, 189, 66],
            'Growing_Days_C/f': [9, 3, 1, 3, 1, 2]
        },
        'Zone G': {
            'Field': ['8', '1', '44', '13', '9', '4'],
            'Leaf_Type': ['VP', 'SD', 'VP', 'VP', 'SD', 'VP'],
            'Ha': [9.07, 17.06, 7.19, 14.34, 20.43, 16.36],
            'Days_to_plk': [1, 2, 1, 1, 2, 2],
            'Prune_age': [3, 1, 2, 1, 3, 3],
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

    Kakuzi_PLC = request.POST.get('kakuzi_plc')
    Kaboswa = request.POST.get('kaboswa')
    Septon = request.POST.get('septon')
    current_month = request.POST.get('month')
    current_year = request.POST.get('year')

    context = {
        "pluckingrounds": table,
        'html': html,
        "company": Kakuzi_PLC,
        "estate": Kaboswa,
        "division": Septon,
        "month": current_month,
        "year": current_year,
    }
    return render(request, 'Plucking/plucking_scheme_rounds.html', context)


def PluckingRoundsViewUpdate(request):
    if request.method == 'POST':
        Field_No = request.POST.get('zone')
        leaf_type = request.POST.get('leaf_type')
        ha = request.POST.get('ha')
        days_to_pluck = request.POST.get('days_to_pluck')
        prune_age = request.POST.get('prune_age')
        number_of_schemes = request.POST.get('number_of_schemes')
        growing_days_cf = request.POST.get('growing_days_cf')
        Month_day_01 = request.POST.get('Month_day_01')
        Month_day_02 = request.POST.get('Month_day_02')
        Month_day_03 = request.POST.get('Month_day_03')
        Month_day_04 = request.POST.get('Month_day_04')
        Month_day_05 = request.POST.get('Month_day_05')
        Month_day_06 = request.POST.get('Month_day_06')
        Month_day_07 = request.POST.get('Month_day_07')
        Month_day_08 = request.POST.get('Month_day_08')
        Month_day_09 = request.POST.get('Month_day_09')
        Month_day_10 = request.POST.get('Month_day_10')
        Month_day_11 = request.POST.get('Month_day_11')
        Month_day_12 = request.POST.get('Month_day_12')
        Month_day_13 = request.POST.get('Month_day_13')
        Month_day_14 = request.POST.get('Month_day_14')
        Month_day_15 = request.POST.get('Month_day_15')
        Month_day_16 = request.POST.get('Month_day_16')
        Month_day_17 = request.POST.get('Month_day_17')
        Month_day_18 = request.POST.get('Month_day_18')
        Month_day_19 = request.POST.get('Month_day_19')
        Month_day_20 = request.POST.get('Month_day_20')
        Month_day_21 = request.POST.get('Month_day_21')
        Month_day_22 = request.POST.get('Month_day_22')
        Month_day_23 = request.POST.get('Month_day_23')
        Month_day_24 = request.POST.get('Month_day_24')
        Month_day_25 = request.POST.get('Month_day_25')
        Month_day_26 = request.POST.get('Month_day_26')
        Month_day_27 = request.POST.get('Month_day_27')
        Month_day_28 = request.POST.get('Month_day_28')
        Month_day_29 = request.POST.get('Month_day_29')
        Month_day_30 = request.POST.get('Month_day_30')
        Month_day_31 = request.POST.get('Month_day_31')
        # Repeat the above lines for each month_day field (month_day_03, month_day_04, ..., month_day_31)

        # Process and update the field in the database
        data = FieldsToPluck.objects.get(id=1)  # Replace <field_id> with the actual ID of the field you want to update
        data.Field_No = Field_No
        data.leaf_type = leaf_type
        data.ha = ha
        data.days_to_pluck = days_to_pluck
        data.prune_age = prune_age
        data.number_of_schemes = number_of_schemes
        data.growing_days_cf = growing_days_cf
        data.Month_day_01 = Month_day_01
        data.Month_day_02 = Month_day_02
        data.Month_day_03 = Month_day_03
        data.Month_day_04 = Month_day_04
        data.Month_day_05 = Month_day_05
        data.Month_day_06 = Month_day_06
        data.Month_day_07 = Month_day_07
        data.Month_day_08 = Month_day_08
        data.Month_day_09 = Month_day_09
        data.Month_day_10 = Month_day_10
        data.Month_day_11 = Month_day_11
        data.Month_day_12 = Month_day_12
        data.Month_day_13 = Month_day_13
        data.Month_day_14 = Month_day_14
        data.Month_day_15 = Month_day_15
        data.Month_day_16 = Month_day_16
        data.Month_day_17 = Month_day_17
        data.Month_day_18 = Month_day_18
        data.Month_day_19 = Month_day_19
        data.Month_day_20 = Month_day_20
        data.Month_day_21 = Month_day_21
        data.Month_day_22 = Month_day_22
        data.Month_day_23 = Month_day_23
        data.Month_day_24 = Month_day_24
        data.Month_day_25 = Month_day_25
        data.Month_day_26 = Month_day_26
        data.Month_day_27 = Month_day_27
        data.Month_day_28 = Month_day_28
        data.Month_day_29 = Month_day_29
        data.Month_day_30 = Month_day_30
        data.Month_day_31 = Month_day_31
        # Repeat the above line for each month_day field (month_day_03, month_day_04, ..., month_day_31)
        data.save()

        return redirect('fields-record')  # Replace 'fields-record' with the actual URL name for the fields record page

    # Retrieve the existing field data for pre-filling the form
    data = FieldsToPluck.objects.get(
        id=1)  # Replace <field_id> with the actual ID of the field you want to update

    context = {
        'Zone': data.Zone,
        'Field_No': data.Field_No,
        'Leaf_Type': data.Leaf_Type,
        'Ha': data.Ha,
        'Days_to_plk': data.Days_to_plk,
        'Prune_age': data.Prune_age,
        'Number_of_schemes': data.Number_of_schemes,
        'Month_day_01': data.Month_day_01,
        'Month_day_02': data.Month_day_02,
        'Month_day_03': data.Month_day_03,
        'Month_day_04': data.Month_day_04,
        'Month_day_05': data.Month_day_05,
        'Month_day_06': data.Month_day_06,
        'Month_day_07': data.Month_day_07,
        'Month_day_08': data.Month_day_08,
        'Month_day_09': data.Month_day_09,
        'Month_day_10': data.Month_day_10,
        'Month_day_11': data.Month_day_11,
        'Month_day_12': data.Month_day_12,
        'Month_day_13': data.Month_day_13,
        'Month_day_14': data.Month_day_14,
        'Month_day_15': data.Month_day_15,
        'Month_day_16': data.Month_day_16,
        'Month_day_17': data.Month_day_17,
        'Month_day_18': data.Month_day_18,
        'Month_day_19': data.Month_day_19,
        'Month_day_20': data.Month_day_20,
        'Month_day_21': data.Month_day_21,
        'Month_day_22': data.Month_day_22,
        'Month_day_23': data.Month_day_23,
        'Month_day_24': data.Month_day_24,
        'Month_day_25': data.Month_day_25,
        'Month_day_26': data.Month_day_26,
        'Month_day_27': data.Month_day_27,
        'Month_day_28': data.Month_day_28,
        'Month_day_29': data.Month_day_29,
        'Month_day_30': data.Month_day_30,
        'Month_day_31': data.Month_day_31,

    }
    return render(request, 'Plucking/plucking_scheme_rounds_update.html', context)
    # return render(request, 'Plucking/psp_fields_rounds_checker-update.html', context)


def PluckingRoundsViewCreate(request):
    if request.method == "POST":
        table = request.POST['table']
        table.save()

    return render(request, 'Plucking/plucking_scheme_rounds.html')


def save_edited_content(request):
    if request.method == 'POST' and request.is_ajax():
        edited_content = request.POST.get('content')
        request.session['editableCellContent'] = edited_content
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})


def FieldsViewRetrieve(request):
    # Retrieve field data from the database
    data = FieldsToPluck.objects.all()

    Division_data = {
        'Zone E': {
            'Field_No': ['5', '3', '7', '12', '14', '15'],
            'Leaf_Type': ['SD', 'SD', 'VP', 'VP', 'VP'],
            'Ha': [13.02, 8.27, 14.99, 12.93, 22.60, 10.65],
            'Days_to_plk': [1, 2, 1, 2, 2, 1],
            'Prune_age': [2, 2, 1, 0, 3, 4],
            'Num_of_Schemes': [185, 145, 92, 152, 323, 167],
            'Growing_days_CF': [1, 2, 1, 2, 1, 0],
            'Month_day_Jan': [31, 31, 31, 31, 31, 31],
            'Month_day_Feb': [28, 28, 28, 28, 28, 28],
            'Month_day_Mar': [31, 31, 31, 31, 31, 31],
            'Month_day_Apr': [30, 30, 30, 30, 30, 30],
            'Month_day_May': [31, 31, 31, 31, 31, 31],
            'Month_day_Jun': [30, 30, 30, 30, 30, 30],
            'Month_day_Jul': [31, 31, 31, 31, 31, 31],
            'Month_day_Aug': [31, 31, 31, 31, 31, 31],
            'Month_day_Sep': [30, 30, 30, 30, 30, 30],
            'Month_day_Oct': [31, 31, 31, 31, 31, 31],
            'Month_day_Nov': [30, 30, 30, 30, 30, 30],
            'Month_day_Dec': [31, 31, 31, 31, 31, 31],
        },
        'Zone F': {
            'Field_No': ['11', '10', '42', '2', '6', '43'],
            'Leaf_Type': ['SD', 'SD', 'VP', 'SD', 'VP'],
            'Ha': [16.01, 22.55, 7.51, 7.41, 17.00, 4.6],
            'Days_to_plk': [2, 3, 1, 1, 2, 1],
            'Prune_age': [2, 1, 3, 1, 0, 1],
            'Num_of_Schemes': [178, 251, 107, 106, 189, 66],
            'Growing_days_CF': [9, 3, 1, 3, 1, 2],
            'Month_day_Jan': [31, 31, 31, 31, 31, 31],
            'Month_day_Feb': [28, 28, 28, 28, 28, 28],
            'Month_day_Mar': [31, 31, 31, 31, 31, 31],
            'Month_day_Apr': [30, 30, 30, 30, 30, 30],
            'Month_day_May': [31, 31, 31, 31, 31, 31],
            'Month_day_Jun': [30, 30, 30, 30, 30, 30],
            'Month_day_Jul': [31, 31, 31, 31, 31, 31],
            'Month_day_Aug': [31, 31, 31, 31, 31, 31],
            'Month_day_Sep': [30, 30, 30, 30, 30, 30],
            'Month_day_Oct': [31, 31, 31, 31, 31, 31],
            'Month_day_Nov': [30, 30, 30, 30, 30, 30],
            'Month_day_Dec': [31, 31, 31, 31, 31, 31],
        },
        'Zone G': {
            'Field_No': ['8', '1', '44', '13', '9', '4'],
            'Leaf_Type': ['VP', 'SD', 'VP', 'VP', 'SD', 'VP'],
            'Ha': [9.07, 17.06, 7.19, 14.34, 20.43, 16.36],
            'Days_to_plk': [1, 2, 1, 1, 2, 2],
            'Prune_age': [3, 1, 2, 1, 3, 3],
            'Num_of_Schemes': [130, 190, 71, 113, 158, 165],
            'Growing_days_CF': [1, 2, 1, 1, 2, 2],
            'Month_day_Jan': [31, 31, 31, 31, 31, 31],
            'Month_day_Feb': [28, 28, 28, 28, 28, 28],
            'Month_day_Mar': [31, 31, 31, 31, 31, 31],
            'Month_day_Apr': [30, 30, 30, 30, 30, 30],
            'Month_day_May': [31, 31, 31, 31, 31, 31],
            'Month_day_Jun': [30, 30, 30, 30, 30, 30],
            'Month_day_Jul': [31, 31, 31, 31, 31, 31],
            'Month_day_Aug': [31, 31, 31, 31, 31, 31],
            'Month_day_Sep': [30, 30, 30, 30, 30, 30],
            'Month_day_Oct': [31, 31, 31, 31, 31, 31],
            'Month_day_Nov': [30, 30, 30, 30, 30, 30],
            'Month_day_Dec': [31, 31, 31, 31, 31, 31],

        },
    }

    Division_data_list = []

    for Division, zone_data in Division_data.items():
        field_indexes = []
        for field_no in zone_data['Field_No']:
            field_index = next(
                (index for index, field in enumerate(data) if field.Field_No == field_no), None)
            if field_index is not None:
                field_indexes.append(field_index)

        for field_index in field_indexes:
            Division_data_list.append({
                'Field_No': zone_data['Field_No'][field_index],
                'Leaf_Type': zone_data['Leaf_Type'][field_index],
                'Ha': zone_data['Ha'][field_index],
                'Days_to_plk': zone_data['Days_to_plk'][field_index],
                'Prune_age': zone_data['Prune_age'][field_index],
                'Num_of_Schemes': zone_data['Num_of_Schemes'][field_index],
                'Growing_days_CF': zone_data['Growing_days_CF'][field_index],
                'Month_day_Jan': zone_data['Month_day_Jan'][field_index],
                'Month_day_Feb': zone_data['Month_day_Feb'][field_index],
                'Month_day_Mar': zone_data['Month_day_Mar'][field_index],
                'Month_day_Apr': zone_data['Month_day_Apr'][field_index],
                'Month_day_May': zone_data['Month_day_May'][field_index],
                'Month_day_Jun': zone_data['Month_day_Jun'][field_index],
                'Month_day_Jul': zone_data['Month_day_Jul'][field_index],
                'Month_day_Aug': zone_data['Month_day_Aug'][field_index],
                'Month_day_Sep': zone_data['Month_day_Sep'][field_index],
                'Month_day_Oct': zone_data['Month_day_Oct'][field_index],
                'Month_day_Nov': zone_data['Month_day_Nov'][field_index],
                'Month_day_Dec': zone_data['Month_day_Dec'][field_index]
            })

    month = 5
    num_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    context = {
        'fieldstopluck': data,
        'Division_data': Division_data_list,
        'num_days': num_days[month]
    }

    return render(request, 'Plucking/psp_field_rounds_checker.html', context)


def FieldsViewUpdate(request):
    data = FieldsToPluck.objects.all()
    Division_data = {
        'Zone E': {
            'Field_No': ['5', '3', '7', '12', '14', '15'],
            'Leaf_Type': ['SD', 'SD', 'VP', 'VP', 'VP'],
            'Ha': [13.02, 8.27, 14.99, 12.93, 22.60, 10.65],
            'Days_to_plk': [1, 2, 1, 2, 2, 1],
            'Prune_age': [2, 2, 1, 0, 3, 4],
            'Num_of_Schemes': [185, 145, 92, 152, 323, 167],
            'Growing_days_CF': [1, 2, 1, 2, 1, 0],
            'Month_day_Jan': [31, 31, 31, 31, 31, 31],
            'Month_day_Feb': [28, 28, 28, 28, 28, 28],
            'Month_day_Mar': [31, 31, 31, 31, 31, 31],
            'Month_day_Apr': [30, 30, 30, 30, 30, 30],
            'Month_day_May': [31, 31, 31, 31, 31, 31],
            'Month_day_Jun': [30, 30, 30, 30, 30, 30],
            'Month_day_Jul': [31, 31, 31, 31, 31, 31],
            'Month_day_Aug': [31, 31, 31, 31, 31, 31],
            'Month_day_Sep': [30, 30, 30, 30, 30, 30],
            'Month_day_Oct': [31, 31, 31, 31, 31, 31],
            'Month_day_Nov': [30, 30, 30, 30, 30, 30],
            'Month_day_Dec': [31, 31, 31, 31, 31, 31],
        },
        'Zone F': {
            'Field_No': ['11', '10', '42', '2', '6', '43'],
            'Leaf_Type': ['SD', 'SD', 'VP', 'SD', 'VP'],
            'Ha': [16.01, 22.55, 7.51, 7.41, 17.00, 4.6],
            'Days_to_plk': [2, 3, 1, 1, 2, 1],
            'Prune_age': [2, 1, 3, 1, 0, 1],
            'Num_of_Schemes': [178, 251, 107, 106, 189, 66],
            'Growing_days_CF': [9, 3, 1, 3, 1, 2],
            'Month_day_Jan': [31, 31, 31, 31, 31, 31],
            'Month_day_Feb': [28, 28, 28, 28, 28, 28],
            'Month_day_Mar': [31, 31, 31, 31, 31, 31],
            'Month_day_Apr': [30, 30, 30, 30, 30, 30],
            'Month_day_May': [31, 31, 31, 31, 31, 31],
            'Month_day_Jun': [30, 30, 30, 30, 30, 30],
            'Month_day_Jul': [31, 31, 31, 31, 31, 31],
            'Month_day_Aug': [31, 31, 31, 31, 31, 31],
            'Month_day_Sep': [30, 30, 30, 30, 30, 30],
            'Month_day_Oct': [31, 31, 31, 31, 31, 31],
            'Month_day_Nov': [30, 30, 30, 30, 30, 30],
            'Month_day_Dec': [31, 31, 31, 31, 31, 31],
        },
        'Zone G': {
            'Field_No': ['8', '1', '44', '13', '9', '4'],
            'Leaf_Type': ['VP', 'SD', 'VP', 'VP', 'SD', 'VP'],
            'Ha': [9.07, 17.06, 7.19, 14.34, 20.43, 16.36],
            'Days_to_plk': [1, 2, 1, 1, 2, 2],
            'Prune_age': [3, 1, 2, 1, 3, 3],
            'Num_of_Schemes': [130, 190, 71, 113, 158, 165],
            'Growing_days_CF': [1, 2, 1, 1, 2, 2],
            'Month_day_Jan': [31, 31, 31, 31, 31, 31],
            'Month_day_Feb': [28, 28, 28, 28, 28, 28],
            'Month_day_Mar': [31, 31, 31, 31, 31, 31],
            'Month_day_Apr': [30, 30, 30, 30, 30, 30],
            'Month_day_May': [31, 31, 31, 31, 31, 31],
            'Month_day_Jun': [30, 30, 30, 30, 30, 30],
            'Month_day_Jul': [31, 31, 31, 31, 31, 31],
            'Month_day_Aug': [31, 31, 31, 31, 31, 31],
            'Month_day_Sep': [30, 30, 30, 30, 30, 30],
            'Month_day_Oct': [31, 31, 31, 31, 31, 31],
            'Month_day_Nov': [30, 30, 30, 30, 30, 30],
            'Month_day_Dec': [31, 31, 31, 31, 31, 31],

        },
    }

    if data:
        zone = data[0].Zone
    else:
        zone = None

    if request.method == 'POST':
        Field_No = request.POST.get('Field_No')  # Retrieve Field_No from POST request
    else:
        Field_No = request.GET.get('Field_No')  # Retrieve Field_No from GET request

    if Field_No is not None:
        field_index = int(Field_No) - 1
    else:
        field_index = None

    zone_data = Division_data.get(zone, {})
    Division_data = {
        'Zone': zone_data.get('Zone', []),
        'Leaf_Type': zone_data.get('Leaf_Type', []),
        'Ha': zone_data.get('Ha', []),
        'Days_to_plk': zone_data.get('Days_to_plk', []),
        'Prune_age': zone_data.get('Prune_age', []),
        'Num_of_Schemes': zone_data.get('Num_of_Schemes', []),
        'Growing_days_CF': zone_data.get('Growing_days_CF', []),
        'Month_day_Jan': zone_data.get('Month_day_Jan', []),
        'Month_day_Feb': zone_data.get('Month_day_Feb', []),
        'Month_day_Mar': zone_data.get('Month_day_Mar', []),
        'Month_day_Apr': zone_data.get('Month_day_Apr', []),
        'Month_day_May': zone_data.get('Month_day_May', []),
        'Month_day_Jun': zone_data.get('Month_day_Jun', []),
        'Month_day_Jul': zone_data.get('Month_day_Jul', []),
        'Month_day_Aug': zone_data.get('Month_day_Aug', []),
        'Month_day_Sep': zone_data.get('Month_day_Sep', []),
        'Month_day_Oct': zone_data.get('Month_day_Oct', []),
        'Month_day_Nov': zone_data.get('Month_day_Nov', []),
        'Month_day_Dec': zone_data.get('Month_day_Dec', []),
    }

    return render(request, 'Plucking/psp_fields_rounds_checker-update.html', {'Division_data': Division_data})


def FieldsViewCreate(request):
    if request.method == "POST":
        Zone = request.POST.get('Zone')
        Field_No = request.POST.get('Field_No')
        Leaf_Type = request.POST.get('Leaf_Type')
        Ha = request.POST.get('Ha')
        Days_to_plk = request.POST.get('Days_to_plk')
        Prune_age = request.POST.get('Prune_age')
        Number_of_schemes = request.POST.get('Number_of_schemes')
        Growing_days_CF = request.POST.get('Growing_days_CF')
        Month_day_01 = request.POST.get('Month_day_01')
        Month_day_02 = request.POST.get('Month_day_02')
        Month_day_03 = request.POST.get('Month_day_03')
        Month_day_04 = request.POST.get('Month_day_04')
        Month_day_05 = request.POST.get('Month_day_05')
        Month_day_06 = request.POST.get('Month_day_06')
        Month_day_07 = request.POST.get('Month_day_07')
        Month_day_08 = request.POST.get('Month_day_08')
        Month_day_09 = request.POST.get('Month_day_09')
        Month_day_10 = request.POST.get('Month_day_10')
        Month_day_11 = request.POST.get('Month_day_11')
        Month_day_12 = request.POST.get('Month_day_12')
        Month_day_13 = request.POST.get('Month_day_13')
        Month_day_14 = request.POST.get('Month_day_14')
        Month_day_15 = request.POST.get('Month_day_15')
        Month_day_16 = request.POST.get('Month_day_16')
        Month_day_17 = request.POST.get('Month_day_17')
        Month_day_18 = request.POST.get('Month_day_18')
        Month_day_19 = request.POST.get('Month_day_19')
        Month_day_20 = request.POST.get('Month_day_20')
        Month_day_21 = request.POST.get('Month_day_21')
        Month_day_22 = request.POST.get('Month_day_22')
        Month_day_23 = request.POST.get('Month_day_23')
        Month_day_24 = request.POST.get('Month_day_24')
        Month_day_25 = request.POST.get('Month_day_25')
        Month_day_26 = request.POST.get('Month_day_26')
        Month_day_27 = request.POST.get('Month_day_27')
        Month_day_28 = request.POST.get('Month_day_28')
        Month_day_29 = request.POST.get('Month_day_29')
        Month_day_30 = request.POST.get('Month_day_30')
        Month_day_31 = request.POST.get('Month_day_31')

        insert = FieldsToPluck(Zone=Zone, Field_No=Field_No, Leaf_Type=Leaf_Type, Ha=Ha, Days_to_plk=Days_to_plk,
                               Prune_age=Prune_age, Number_of_schemes=Number_of_schemes,
                               Growing_days_CF=Growing_days_CF, Month_day_01=Month_day_01,
                               Month_day_02=Month_day_02, Month_day_03=Month_day_03, Month_day_04=Month_day_04,
                               Month_day_05=Month_day_05, Month_day_06=Month_day_06, Month_day_07=Month_day_07,
                               Month_day_08=Month_day_08, Month_day_09=Month_day_09, Month_day_10=Month_day_10,
                               Month_day_11=Month_day_11, Month_day_12=Month_day_12, Month_day_13=Month_day_13,
                               Month_day_14=Month_day_14, Month_day_15=Month_day_15, Month_day_16=Month_day_16,
                               Month_day_17=Month_day_17, Month_day_18=Month_day_18, Month_day_19=Month_day_19,
                               Month_day_20=Month_day_20, Month_day_21=Month_day_21, Month_day_22=Month_day_22,
                               Month_day_23=Month_day_23, Month_day_24=Month_day_24, Month_day_25=Month_day_25,
                               Month_day_26=Month_day_26, Month_day_27=Month_day_27, Month_day_28=Month_day_28,
                               Month_day_29=Month_day_29, Month_day_30=Month_day_30, Month_day_31=Month_day_31)
        insert.save()

    return redirect('/fields-record')


def FieldsEdit(request, pk):
    fields = FieldsToPluck.objects.get(id=pk)
    if request.method == 'POST':
        form = FieldsForm(request.POST, instance=fields)
        if form.is_valid():
            form.save()
            return redirect('/fields-record')

    else:
        form = FieldsForm(instance=fields)

    context = {
        'form': form, 'FieldsForm': FieldsForm,

    }
    return render(request, 'Fields/update.html', context)


def FieldsDelete(request, pk):
    data = FieldsToPluck.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('/fields-record')

    context = {
        'data': data,
    }
    return render(request, 'Fields/delete.html', context)


def AutoFieldsViewRetrieve(request):
    # Retrieve field data from the database
    data = AutoFields.objects.all()

    Zone_E_data = {
                      'Field_No': ['5', '3', '7', '12', '14', '15'],
                      'Leaf_type': ['SD', 'SD', 'VP', 'VP', 'VP'],
                      'Ha': [13.02, 8.27, 14.99, 12.93, 22.60, 10.65],
                      'Days_to_plk': [1, 2, 1, 2, 2, 1],
                      'Prune_age': [2, 2, 1, 0, 3, 4],
                      'Num_of_Schemes': [185, 145, 92, 152, 323, 167],
                      'Growing_days_CF': [1, 2, 1, 2, 1, 0],
                      'Month_day_Jan': [31, 31, 31, 31, 31, 31],
                      'Month_day_Feb': [28, 28, 28, 28, 28, 28],
                      'Month_day_Mar': [31, 31, 31, 31, 31, 31],
                      'Month_day_Apr': [30, 30, 30, 30, 30, 30],
                      'Month_day_May': [31, 31, 31, 31, 31, 31],
                      'Month_day_Jun': [30, 30, 30, 30, 30, 30],
                      'Month_day_Jul': [31, 31, 31, 31, 31, 31],
                      'Month_day_Aug': [31, 31, 31, 31, 31, 31],
                      'Month_day_Sep': [30, 30, 30, 30, 30, 30],
                      'Month_day_Oct': [31, 31, 31, 31, 31, 31],
                      'Month_day_Nov': [30, 30, 30, 30, 30, 30],
                      'Month_day_Dec': [31, 31, 31, 31, 31, 31],
                  },
    Zone_F_data = {
                      'Field_No': ['11', '10', '42', '2', '6', '43'],
                      'Leaf_type': ['SD', 'SD', 'VP', 'SD', 'VP'],
                      'Ha': [16.01, 22.55, 7.51, 7.41, 17.00, 4.6],
                      'Days_to_plk': [2, 3, 1, 1, 2, 1],
                      'Prune_age': [2, 1, 3, 1, 0, 1],
                      'Num_of_Schemes': [178, 251, 107, 106, 189, 66],
                      'Growing_days_CF': [9, 3, 1, 3, 1, 2],
                      'Month_day_Jan': [31, 31, 31, 31, 31, 31],
                      'Month_day_Feb': [28, 28, 28, 28, 28, 28],
                      'Month_day_Mar': [31, 31, 31, 31, 31, 31],
                      'Month_day_Apr': [30, 30, 30, 30, 30, 30],
                      'Month_day_May': [31, 31, 31, 31, 31, 31],
                      'Month_day_Jun': [30, 30, 30, 30, 30, 30],
                      'Month_day_Jul': [31, 31, 31, 31, 31, 31],
                      'Month_day_Aug': [31, 31, 31, 31, 31, 31],
                      'Month_day_Sep': [30, 30, 30, 30, 30, 30],
                      'Month_day_Oct': [31, 31, 31, 31, 31, 31],
                      'Month_day_Nov': [30, 30, 30, 30, 30, 30],
                      'Month_day_Dec': [31, 31, 31, 31, 31, 31],
                  },
    Zone_G_data = {
                      'Field_No': ['8', '1', '44', '13', '9', '4'],
                      'Leaf_type': ['VP', 'SD', 'VP', 'VP', 'SD', 'VP'],
                      'Ha': [9.07, 17.06, 7.19, 14.34, 20.43, 16.36],
                      'Days_to_plk': [1, 2, 1, 1, 2, 2],
                      'Prune_age': [3, 1, 2, 1, 3, 3],
                      'Num_of_Schemes': [130, 190, 71, 113, 158, 165],
                      'Growing_days_CF': [1, 2, 1, 1, 2, 2],
                      'Month_day_Jan': [31, 31, 31, 31, 31, 31],
                      'Month_day_Feb': [28, 28, 28, 28, 28, 28],
                      'Month_day_Mar': [31, 31, 31, 31, 31, 31],
                      'Month_day_Apr': [30, 30, 30, 30, 30, 30],
                      'Month_day_May': [31, 31, 31, 31, 31, 31],
                      'Month_day_Jun': [30, 30, 30, 30, 30, 30],
                      'Month_day_Jul': [31, 31, 31, 31, 31, 31],
                      'Month_day_Aug': [31, 31, 31, 31, 31, 31],
                      'Month_day_Sep': [30, 30, 30, 30, 30, 30],
                      'Month_day_Oct': [31, 31, 31, 31, 31, 31],
                      'Month_day_Nov': [30, 30, 30, 30, 30, 30],
                      'Month_day_Dec': [31, 31, 31, 31, 31, 31],

                  },

    field_list = []
    for zone_data in [Zone_E_data, Zone_F_data, Zone_G_data]:
        zone_fields = []
        for i in range(len(zone_data)):
            field = {
                'Field_No': zone_data[i]['Field_No'],
                'Leaf_type': zone_data[i]['Leaf_type'],
                'Ha': zone_data[i]['Ha'],
                'Days_to_plk': zone_data[i]['Days_to_plk'],
                'Prune_age': zone_data[i]['Prune_age'],
                'Num_of_Schemes': zone_data[i]['Num_of_Schemes'],
                'Growing_days_CF': zone_data[i]['Growing_days_CF'],
                'Month_day_Jan': zone_data[i]['Month_day_Jan'],
                'Month_day_Feb': zone_data[i]['Month_day_Feb'],
                'Month_day_Mar': zone_data[i]['Month_day_Mar'],
                'Month_day_Apr': zone_data[i]['Month_day_Apr'],
                'Month_day_May': zone_data[i]['Month_day_May'],
                'Month_day_Jun': zone_data[i]['Month_day_Jun'],
                'Month_day_Jul': zone_data[i]['Month_day_Jul'],
                'Month_day_Aug': zone_data[i]['Month_day_Aug'],
                'Month_day_Sep': zone_data[i]['Month_day_Sep'],
                'Month_day_Oct': zone_data[i]['Month_day_Oct'],
                'Month_day_Nov': zone_data[i]['Month_day_Nov'],
                'Month_day_Dec': zone_data[i]['Month_day_Dec'],
            }
            field_list.append(field)

    month = 5
    num_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    rows = [
        [6, 1],
        [5, None, 2],
        [5, None, 2],
        [4, None, None, 3],
        [3, None, None, 4],
        [3, None, None, 4, 5],
        [2, None, None, None, None, 6],
        [0, None, None, None, None, None, 7],
        [0, None, None, None, None, None, 7]
    ]

    num_columns = max(len(row) for row in rows)

    for row in rows:
        while len(row) < num_columns:
            row.insert(1, None)

    context = {
        'autofields': data,
        'num_days': num_days[month],
        'rows': rows,
        'num_columns': num_columns
    }

    return render(request, 'Plucking/autofields_psp.html', context)


def AutoFieldsViewUpdate(request):
    data = AutoFields.objects.all()
    Division_data = {
        'Zone_E': {
            'Field_No': ['5', '3', '7', '12', '14', '15'],
            'Leaf_type': ['SD', 'SD', 'VP', 'VP', 'VP'],
            'Ha': [13.02, 8.27, 14.99, 12.93, 22.60, 10.65],
            'Days_to_plk': [1, 2, 1, 2, 2, 1],
            'Prune_age': [2, 2, 1, 0, 3, 4],
            'Num_of_Schemes': [185, 145, 92, 152, 323, 167],
            'Growing_days_CF': [1, 2, 1, 2, 1, 0],
            'Month_day_Jan': [31, 31, 31, 31, 31, 31],
            'Month_day_Feb': [28, 28, 28, 28, 28, 28],
            'Month_day_Mar': [31, 31, 31, 31, 31, 31],
            'Month_day_Apr': [30, 30, 30, 30, 30, 30],
            'Month_day_May': [31, 31, 31, 31, 31, 31],
            'Month_day_Jun': [30, 30, 30, 30, 30, 30],
            'Month_day_Jul': [31, 31, 31, 31, 31, 31],
            'Month_day_Aug': [31, 31, 31, 31, 31, 31],
            'Month_day_Sep': [30, 30, 30, 30, 30, 30],
            'Month_day_Oct': [31, 31, 31, 31, 31, 31],
            'Month_day_Nov': [30, 30, 30, 30, 30, 30],
            'Month_day_Dec': [31, 31, 31, 31, 31, 31],
        },
        'Zone_F': {
            'Field_No': ['11', '10', '42', '2', '6', '43'],
            'Leaf_type': ['SD', 'SD', 'VP', 'SD', 'VP'],
            'Ha': [16.01, 22.55, 7.51, 7.41, 17.00, 4.6],
            'Days_to_plk': [2, 3, 1, 1, 2, 1],
            'Prune_age': [2, 1, 3, 1, 0, 1],
            'Num_of_Schemes': [178, 251, 107, 106, 189, 66],
            'Growing_days_CF': [9, 3, 1, 3, 1, 2],
            'Month_day_Jan': [31, 31, 31, 31, 31, 31],
            'Month_day_Feb': [28, 28, 28, 28, 28, 28],
            'Month_day_Mar': [31, 31, 31, 31, 31, 31],
            'Month_day_Apr': [30, 30, 30, 30, 30, 30],
            'Month_day_May': [31, 31, 31, 31, 31, 31],
            'Month_day_Jun': [30, 30, 30, 30, 30, 30],
            'Month_day_Jul': [31, 31, 31, 31, 31, 31],
            'Month_day_Aug': [31, 31, 31, 31, 31, 31],
            'Month_day_Sep': [30, 30, 30, 30, 30, 30],
            'Month_day_Oct': [31, 31, 31, 31, 31, 31],
            'Month_day_Nov': [30, 30, 30, 30, 30, 30],
            'Month_day_Dec': [31, 31, 31, 31, 31, 31],
        },
        'Zone_G': {
            'Field_No': ['8', '1', '44', '13', '9', '4'],
            'Leaf_type': ['VP', 'SD', 'VP', 'VP', 'SD', 'VP'],
            'Ha': [9.07, 17.06, 7.19, 14.34, 20.43, 16.36],
            'Days_to_plk': [1, 2, 1, 1, 2, 2],
            'Prune_age': [3, 1, 2, 1, 3, 3],
            'Num_of_Schemes': [130, 190, 71, 113, 158, 165],
            'Growing_days_CF': [1, 2, 1, 1, 2, 2],
            'Month_day_Jan': [31, 31, 31, 31, 31, 31],
            'Month_day_Feb': [28, 28, 28, 28, 28, 28],
            'Month_day_Mar': [31, 31, 31, 31, 31, 31],
            'Month_day_Apr': [30, 30, 30, 30, 30, 30],
            'Month_day_May': [31, 31, 31, 31, 31, 31],
            'Month_day_Jun': [30, 30, 30, 30, 30, 30],
            'Month_day_Jul': [31, 31, 31, 31, 31, 31],
            'Month_day_Aug': [31, 31, 31, 31, 31, 31],
            'Month_day_Sep': [30, 30, 30, 30, 30, 30],
            'Month_day_Oct': [31, 31, 31, 31, 31, 31],
            'Month_day_Nov': [30, 30, 30, 30, 30, 30],
            'Month_day_Dec': [31, 31, 31, 31, 31, 31],

        },
    }

    if data:
        zone = data[0].Zone
    else:
        zone = None

    if request.method == 'POST':
        Field_No = request.POST.get('Field_No')  # Retrieve Field_No from POST request
    else:
        Field_No = request.GET.get('Field_No')  # Retrieve Field_No from GET request

    if Field_No is not None:
        field_index = int(Field_No) - 1
    else:
        field_index = None

    zone_data = Division_data.get(zone, {})
    Division_data = {
        'Zone': zone_data.get('Zone_E', []),
        'Leaf_type': zone_data.get('Leaf_type', []),
        'Ha': zone_data.get('Ha', []),
        'Days_to_plk': zone_data.get('Days_to_plk', []),
        'Prune_age': zone_data.get('Prune_age', []),
        'Num_of_Schemes': zone_data.get('Num_of_Schemes', []),
        'Growing_days_CF': zone_data.get('Growing_days_CF', []),
        'Month_day_Jan': zone_data.get('Month_day_Jan', []),
        'Month_day_Feb': zone_data.get('Month_day_Feb', []),
        'Month_day_Mar': zone_data.get('Month_day_Mar', []),
        'Month_day_Apr': zone_data.get('Month_day_Apr', []),
        'Month_day_May': zone_data.get('Month_day_May', []),
        'Month_day_Jun': zone_data.get('Month_day_Jun', []),
        'Month_day_Jul': zone_data.get('Month_day_Jul', []),
        'Month_day_Aug': zone_data.get('Month_day_Aug', []),
        'Month_day_Sep': zone_data.get('Month_day_Sep', []),
        'Month_day_Oct': zone_data.get('Month_day_Oct', []),
        'Month_day_Nov': zone_data.get('Month_day_Nov', []),
        'Month_day_Dec': zone_data.get('Month_day_Dec', []),
    }

    if data:
        zone = data[0].Zone
    else:
        zone = None

    if request.method == 'POST':
        Field_No = request.POST.get('Field_No')  # Retrieve Field_No from POST request
    else:
        Field_No = request.GET.get('Field_No')  # Retrieve Field_No from GET request

    if Field_No is not None:
        field_index = int(Field_No) - 1
    else:
        field_index = None

    zone_data = Division_data.get(zone, {})
    Division_data = {
        'Zone': zone_data.get('Zone_F', []),
        'Leaf_type': zone_data.get('Leaf_type', []),
        'Ha': zone_data.get('Ha', []),
        'Days_to_plk': zone_data.get('Days_to_plk', []),
        'Prune_age': zone_data.get('Prune_age', []),
        'Num_of_Schemes': zone_data.get('Num_of_Schemes', []),
        'Growing_days_CF': zone_data.get('Growing_days_CF', []),
        'Month_day_Jan': zone_data.get('Month_day_Jan', []),
        'Month_day_Feb': zone_data.get('Month_day_Feb', []),
        'Month_day_Mar': zone_data.get('Month_day_Mar', []),
        'Month_day_Apr': zone_data.get('Month_day_Apr', []),
        'Month_day_May': zone_data.get('Month_day_May', []),
        'Month_day_Jun': zone_data.get('Month_day_Jun', []),
        'Month_day_Jul': zone_data.get('Month_day_Jul', []),
        'Month_day_Aug': zone_data.get('Month_day_Aug', []),
        'Month_day_Sep': zone_data.get('Month_day_Sep', []),
        'Month_day_Oct': zone_data.get('Month_day_Oct', []),
        'Month_day_Nov': zone_data.get('Month_day_Nov', []),
        'Month_day_Dec': zone_data.get('Month_day_Dec', []),
    }

    if data:
        zone = data[0].Zone
    else:
        zone = None

    if request.method == 'POST':
        Field_No = request.POST.get('Field_No')  # Retrieve Field_No from POST request
    else:
        Field_No = request.GET.get('Field_No')  # Retrieve Field_No from GET request

    if Field_No is not None:
        field_index = int(Field_No) - 1
    else:
        field_index = None

    zone_data = Division_data.get(zone, {})
    Division_data = {
        'Zone_G': zone_data.get('Zone_G', []),
        'Leaf_type': zone_data.get('Leaf_type', []),
        'Ha': zone_data.get('Ha', []),
        'Days_to_plk': zone_data.get('Days_to_plk', []),
        'Prune_age': zone_data.get('Prune_age', []),
        'Num_of_Schemes': zone_data.get('Num_of_Schemes', []),
        'Growing_days_CF': zone_data.get('Growing_days_CF', []),
        'Month_day_Jan': zone_data.get('Month_day_Jan', []),
        'Month_day_Feb': zone_data.get('Month_day_Feb', []),
        'Month_day_Mar': zone_data.get('Month_day_Mar', []),
        'Month_day_Apr': zone_data.get('Month_day_Apr', []),
        'Month_day_May': zone_data.get('Month_day_May', []),
        'Month_day_Jun': zone_data.get('Month_day_Jun', []),
        'Month_day_Jul': zone_data.get('Month_day_Jul', []),
        'Month_day_Aug': zone_data.get('Month_day_Aug', []),
        'Month_day_Sep': zone_data.get('Month_day_Sep', []),
        'Month_day_Oct': zone_data.get('Month_day_Oct', []),
        'Month_day_Nov': zone_data.get('Month_day_Nov', []),
        'Month_day_Dec': zone_data.get('Month_day_Dec', []),
    }

    return render(request, 'Plucking/autofields_psp_update.html', {'Division_data': Division_data})


def AutoFieldsViewCreate(request):
    if request.method == "POST":
        Zone = request.POST.get('Zone')
        Field_No = request.POST.get('Field_No')
        Leaf_type = request.POST.get('Leaf_type')
        Ha = request.POST.get('Ha')
        Days_to_plk = request.POST.get('Days_to_plk')
        Prune_age = request.POST.get('Prune_age')
        Number_of_schemes = request.POST.get('Number_of_schemes')
        Growing_days_CF = request.POST.get('Growing_days_CF')
        Month_day_01 = request.POST.get('Month_day_01')
        Month_day_02 = request.POST.get('Month_day_02')
        Month_day_03 = request.POST.get('Month_day_03')
        Month_day_04 = request.POST.get('Month_day_04')
        Month_day_05 = request.POST.get('Month_day_05')
        Month_day_06 = request.POST.get('Month_day_06')
        Month_day_07 = request.POST.get('Month_day_07')
        Month_day_08 = request.POST.get('Month_day_08')
        Month_day_09 = request.POST.get('Month_day_09')
        Month_day_10 = request.POST.get('Month_day_10')
        Month_day_11 = request.POST.get('Month_day_11')
        Month_day_12 = request.POST.get('Month_day_12')
        Month_day_13 = request.POST.get('Month_day_13')
        Month_day_14 = request.POST.get('Month_day_14')
        Month_day_15 = request.POST.get('Month_day_15')
        Month_day_16 = request.POST.get('Month_day_16')
        Month_day_17 = request.POST.get('Month_day_17')
        Month_day_18 = request.POST.get('Month_day_18')
        Month_day_19 = request.POST.get('Month_day_19')
        Month_day_20 = request.POST.get('Month_day_20')
        Month_day_21 = request.POST.get('Month_day_21')
        Month_day_22 = request.POST.get('Month_day_22')
        Month_day_23 = request.POST.get('Month_day_23')
        Month_day_24 = request.POST.get('Month_day_24')
        Month_day_25 = request.POST.get('Month_day_25')
        Month_day_26 = request.POST.get('Month_day_26')
        Month_day_27 = request.POST.get('Month_day_27')
        Month_day_28 = request.POST.get('Month_day_28')
        Month_day_29 = request.POST.get('Month_day_29')
        Month_day_30 = request.POST.get('Month_day_30')
        Month_day_31 = request.POST.get('Month_day_31')

        insert = AutoFields(Zone=Zone, Field_No=Field_No, Leaf_type=Leaf_type, Ha=Ha,
                            Days_to_plk=Days_to_plk, Prune_age=Prune_age, Number_of_schemes=Number_of_schemes,
                            Growing_days_CF=Growing_days_CF, Month_day_01=Month_day_01,
                            Month_day_02=Month_day_02, Month_day_03=Month_day_03, Month_day_04=Month_day_04,
                            Month_day_05=Month_day_05, Month_day_06=Month_day_06, Month_day_07=Month_day_07,
                            Month_day_08=Month_day_08, Month_day_09=Month_day_09, Month_day_10=Month_day_10,
                            Month_day_11=Month_day_11, Month_day_12=Month_day_12, Month_day_13=Month_day_13,
                            Month_day_14=Month_day_14, Month_day_15=Month_day_15, Month_day_16=Month_day_16,
                            Month_day_17=Month_day_17, Month_day_18=Month_day_18, Month_day_19=Month_day_19,
                            Month_day_20=Month_day_20, Month_day_21=Month_day_21, Month_day_22=Month_day_22,
                            Month_day_23=Month_day_23, Month_day_24=Month_day_24, Month_day_25=Month_day_25,
                            Month_day_26=Month_day_26, Month_day_27=Month_day_27, Month_day_28=Month_day_28,
                            Month_day_29=Month_day_29, Month_day_30=Month_day_30, Month_day_31=Month_day_31)
        insert.save()

    return redirect('/autofields-record')


def AutoFieldsEdit(request, pk):
    fields = AutoFields.objects.get(id=pk)
    if request.method == 'POST':
        form = FieldsForms(request.POST, instance=fields)
        if form.is_valid():
            form.save()
            return redirect('/autofields-record')

    else:
        form = FieldsForms(instance=fields)

    context = {
        'form': form, 'FieldsForms': FieldsForms,

    }
    return render(request, 'Autofields/update.html', context)


def AutoFieldsDelete(request, pk):
    data = AutoFields.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('/autofields-record')

    context = {
        'data': data,
    }
    return render(request, 'Autofields/delete.html', context)


def TeaPluckingCycleViewRetrieve(request):
    table_data = [
        {
            'Zone': 'ZONE E',
            'Fields': '14',
            'Growing_Days_CF': [8, 1, 2],
            'Daily_Actual': [1, 2, None, None, None, None, None, None, 1, 2, None, None, None, None, None, None, 1, 2,
                             None, None, None, None, None, None, 1, 2, None, None, None, None, None, None]
        },
        {
            'Zone': 'ZONE E',
            'Fields': '15',
            'Growing_Days_CF': [6, None, None, 3],
            'Daily_Actual': [None, None, 3, None, None, None, None, None, None, None, None, 3, None, None, None, None,
                             None, None, None, None, None, None, 3, None, None, None, None, None, None, None, None]
        },
        {
            'Zone': 'ZONE E',
            'Fields': '5',
            'Growing_Days_CF': [4, None, None, None, 4, 5],
            'Daily_Actual': [None, None, None, None, 4, 5, None, None, None, None, None, None, 4, 5, None, None, None,
                             None, 4, 5, None, None, None, None, 4, 5, None, None, None, None]
        },
        {
            'Zone': 'ZONE E',
            'Fields': '3',
            'Growing_Days_CF': [3, None, None, None, None, None, 6],
            'Daily_Actual': [None, None, None, None, None, None, 6, None, None, None, None, None, None, None, 6, None,
                             None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        },
        {
            'Zone': 'ZONE E',
            'Fields': '7',
            'Growing_Days_CF': [2, None, None, None, None, 6, 7],
            'Daily_Actual': [None, None, None, None, None, 6, 7, None, None, None, None, None, None, None, None, 6, 7,
                             None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        },
        {
            'Zone': 'ZONE E',
            'Fields': '12',
            'Growing_Days_CF': [1, None, None, None, None, None, None, 7],
            'Daily_Actual': [None, None, None, None, None, None, None, 7, None, None, None, None, None, None, None,
                             None, None, 7, None, None, None, None, None, None, None, None, None, None, None, None,
                             None]
        },
        {
            'Zone': 'ZONE F',
            'Fields': '10',
            'Growing_Days_CF': [8, 1, 2],
            'Daily_Actual': [1, 2, None, None, None, None, None, None, 1, 2, None, None, None, None, None, None, 1, 2,
                             None, None, None, None, None, None, 1, 2, None, None, None, None, None, None]
        },
        {
            'Zone': 'ZONE F',
            'Fields': '42',
            'Growing_Days_CF': [6, None, None, 3],
            'Daily_Actual': [None, None, 3, None, None, None, None, None, None, None, None, 3, None, None, None, None,
                             None, None, None, None, None, None, 3, None, None, None, None, None, None, None, None]
        },
        {
            'Zone': 'ZONE F',
            'Fields': '2',
            'Growing_Days_CF': [4, None, None, None, None, None, 4],
            'Daily_Actual': [None, None, None, None, None, None, 4, None, None, None, None, None, None, None, 4, None,
                             None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        },
        {
            'Zone': 'ZONE F',
            'Fields': '6',
            'Growing_Days_CF': [3, None, None, 5, 6],
            'Daily_Actual': [None, None, 5, 6, None, None, None, None, None, 5, 6, None, None, None, None, 5, 6, None,
                             None, None, None, 5, 6, None, None, None, None, 5, 6, None, None]
        },
        {
            'Zone': 'ZONE F',
            'Fields': '43',
            'Growing_Days_CF': [2, None, None, 6, 7],
            'Daily_Actual': [None, None, 6, 7, None, None, None, None, None, 6, 7, None, None, None, None, 6, 7, None,
                             None, None, None, 6, 7, None, None, None, None, 6, 7, None, None]
        },
        {
            'Zone': 'ZONE F',
            'Fields': '11',
            'Growing_Days_CF': [1, None, None, 7],
            'Daily_Actual': [None, None, 7, None, None, None, None, None, None, None, None, 7, None, None, None, None,
                             None, None, None, None, None, None, 7, None, None, None, None, None, None, None]
        },
        {
            'Zone': 'ZONE G',
            'Fields': '44',
            'Growing_Days_CF': [8, None, None, None, None, None, None, None, 1],
            'Daily_Actual': [None, None, None, None, None, None, None, None, 1, None, None, None, None, None, None,
                             None, 1, None, None, None, None, None, None, None, 1, None, None, None, None, None, None]
        },
        {
            'Zone': 'ZONE G',
            'Fields': '13',
            'Growing_Days_CF': [8, None, None, None, None, None, None, None, 1],
            'Daily_Actual': [None, None, None, None, None, None, None, None, 1, None, None, None, None, None, None,
                             None, 1, None, None, None, None, None, None, None, 1, None, None, None, None, None, None]
        },
        {
            'Zone': 'ZONE G',
            'Fields': '9',
            'Growing_Days_CF': [6, None, None, 2, 3],
            'Daily_Actual': [None, None, 2, 3, None, None, None, None, None, 2, 3, None, None, None, None, 2, 3, None,
                             None, None, None, 2, 3, None, None, None, None, 2, 3, None, None]
        },
        {
            'Zone': 'ZONE G',
            'Fields': '4',
            'Growing_Days_CF': [4, None, None, None, 4, 5],
            'Daily_Actual': [None, None, None, None, 4, 5, None, None, None, None, None, None, 4, 5, None, None, None,
                             None, 4, 5, None, None, None, None, 4, 5, None, None, None, None]
        },
        {
            'Zone': 'ZONE G',
            'Fields': '8',
            'Growing_Days_CF': [2, None, None, None, 5, 6],
            'Daily_Actual': [None, None, None, None, 5, 6, None, None, None, None, None, None, 5, 6, None, None, None,
                             None, 5, 6, None, None, None, None, 5, 6, None, None, None, None]
        },
        {
            'Zone': 'ZONE G',
            'Fields': '1',
            'Growing_Days_CF': [1, None, None, None, None, None, None, 7],
            'Daily_Actual': [None, None, None, None, None, None, None, 7, None, None, None, None, None, None, None, 7,
                             None, None, None, None, None, None, 7, None, None, None, None, None, None, None]
        },
    ]

    context = {

        'table_data': table_data,
    }

    return render(request, 'Plucking/tea_plucking_cycle.html', context)


def TeaPluckingCycleViewUpdate(request):
    table_data = []  # Default value for table_data
    table_data = [
        {
            'Zone': 'ZONE E',
            'Fields': '14',
            'Growing_Days_CF': [8, 1, 2],
            'Daily_Actual': [1, 2, None, None, None, None, None, None, 1, 2, None, None, None, None, None, None, 1, 2,
                             None, None, None, None, None, None, 1, 2, None, None, None, None, None, None]
        },
        {
            'Zone': 'ZONE E',
            'Fields': '15',
            'Growing_Days_CF': [6, None, None, 3],
            'Daily_Actual': [None, None, 3, None, None, None, None, None, None, None, None, 3, None, None, None, None,
                             None, None, None, None, None, None, 3, None, None, None, None, None, None, None, None]
        },
        {
            'Zone': 'ZONE E',
            'Fields': '5',
            'Growing_Days_CF': [4, None, None, None, 4, 5],
            'Daily_Actual': [None, None, None, None, 4, 5, None, None, None, None, None, None, 4, 5, None, None, None,
                             None, 4, 5, None, None, None, None, 4, 5, None, None, None, None]
        },
        {
            'Zone': 'ZONE E',
            'Fields': '3',
            'Growing_Days_CF': [3, None, None, None, None, None, 6],
            'Daily_Actual': [None, None, None, None, None, None, 6, None, None, None, None, None, None, None, 6, None,
                             None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        },
        {
            'Zone': 'ZONE E',
            'Fields': '7',
            'Growing_Days_CF': [2, None, None, None, None, 6, 7],
            'Daily_Actual': [None, None, None, None, None, 6, 7, None, None, None, None, None, None, None, None, 6, 7,
                             None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        },
        {
            'Zone': 'ZONE E',
            'Fields': '12',
            'Growing_Days_CF': [1, None, None, None, None, None, None, 7],
            'Daily_Actual': [None, None, None, None, None, None, None, 7, None, None, None, None, None, None, None,
                             None, None, 7, None, None, None, None, None, None, None, None, None, None, None, None,
                             None]
        },
        {
            'Zone': 'ZONE F',
            'Fields': '10',
            'Growing_Days_CF': [8, 1, 2],
            'Daily_Actual': [1, 2, None, None, None, None, None, None, 1, 2, None, None, None, None, None, None, 1, 2,
                             None, None, None, None, None, None, 1, 2, None, None, None, None, None, None]
        },
        {
            'Zone': 'ZONE F',
            'Fields': '42',
            'Growing_Days_CF': [6, None, None, 3],
            'Daily_Actual': [None, None, 3, None, None, None, None, None, None, None, None, 3, None, None, None, None,
                             None, None, None, None, None, None, 3, None, None, None, None, None, None, None, None]
        },
        {
            'Zone': 'ZONE F',
            'Fields': '2',
            'Growing_Days_CF': [4, None, None, None, None, None, 4],
            'Daily_Actual': [None, None, None, None, None, None, 4, None, None, None, None, None, None, None, 4, None,
                             None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        },
        {
            'Zone': 'ZONE F',
            'Fields': '6',
            'Growing_Days_CF': [3, None, None, 5, 6],
            'Daily_Actual': [None, None, 5, 6, None, None, None, None, None, 5, 6, None, None, None, None, 5, 6, None,
                             None, None, None, 5, 6, None, None, None, None, 5, 6, None, None]
        },
        {
            'Zone': 'ZONE F',
            'Fields': '43',
            'Growing_Days_CF': [2, None, None, 6, 7],
            'Daily_Actual': [None, None, 6, 7, None, None, None, None, None, 6, 7, None, None, None, None, 6, 7, None,
                             None, None, None, 6, 7, None, None, None, None, 6, 7, None, None]
        },
        {
            'Zone': 'ZONE F',
            'Fields': '11',
            'Growing_Days_CF': [1, None, None, 7],
            'Daily_Actual': [None, None, 7, None, None, None, None, None, None, None, None, 7, None, None, None, None,
                             None, None, None, None, None, None, 7, None, None, None, None, None, None, None]
        },
        {
            'Zone': 'ZONE G',
            'Fields': '44',
            'Growing_Days_CF': [8, None, None, None, None, None, None, None, 1],
            'Daily_Actual': [None, None, None, None, None, None, None, None, 1, None, None, None, None, None, None,
                             None, 1, None, None, None, None, None, None, None, 1, None, None, None, None, None, None]
        },
        {
            'Zone': 'ZONE G',
            'Fields': '13',
            'Growing_Days_CF': [8, None, None, None, None, None, None, None, 1],
            'Daily_Actual': [None, None, None, None, None, None, None, None, 1, None, None, None, None, None, None,
                             None, 1, None, None, None, None, None, None, None, 1, None, None, None, None, None, None]
        },
        {
            'Zone': 'ZONE G',
            'Fields': '9',
            'Growing_Days_CF': [6, None, None, 2, 3],
            'Daily_Actual': [None, None, 2, 3, None, None, None, None, None, 2, 3, None, None, None, None, 2, 3, None,
                             None, None, None, 2, 3, None, None, None, None, 2, 3, None, None]
        },
        {
            'Zone': 'ZONE G',
            'Fields': '4',
            'Growing_Days_CF': [4, None, None, None, 4, 5],
            'Daily_Actual': [None, None, None, None, 4, 5, None, None, None, None, None, None, 4, 5, None, None, None,
                             None, 4, 5, None, None, None, None, 4, 5, None, None, None, None]
        },
        {
            'Zone': 'ZONE G',
            'Fields': '8',
            'Growing_Days_CF': [2, None, None, None, 5, 6],
            'Daily_Actual': [None, None, None, None, 5, 6, None, None, None, None, None, None, 5, 6, None, None, None,
                             None, 5, 6, None, None, None, None, 5, 6, None, None, None, None]
        },
        {
            'Zone': 'ZONE G',
            'Fields': '1',
            'Growing_Days_CF': [1, None, None, None, None, None, None, 7],
            'Daily_Actual': [None, None, None, None, None, None, None, 7, None, None, None, None, None, None, None, 7,
                             None, None, None, None, None, None, 7, None, None, None, None, None, None, None]
        },
    ]
    if request.method == 'POST':
        # Retrieve the updated values from the request
        updated_data = {
            'Zone': request.POST.get('Zone'),
            'Fields': request.POST.get('Fields'),
            'Growing_Days_CF': [int(day) if day else None for day in request.POST.getlist('Growing_days_CF')],
            'Daily_Actual': [int(actual) if actual else None for actual in request.POST.getlist('Daily_Actual')],
        }

        # Update the existing data with the updated values
        for i, data in enumerate(table_data):
            if i < len(updated_data):
                updated_item = updated_data[i]
                data['Growing_Days_CF'] = updated_item.get('Growing_Days_CF', data['Growing_Days_CF'])
                data['Daily_Actual'] = updated_item.get('Daily_Actual', data['Daily_Actual'])

        # Perform any necessary validation or database updates here

    context = {
        'table_data': table_data,
    }

    return render(request, 'Plucking/tea_plucking_cycle_update.html', context)


def TeaPluckingCycleViewCreate(request):
    if request.method == "POST":
        Zone = request.POST.get('Zone')
        Fields = request.POST.get('Fields')
        Growing_days_CF = request.POST.get('Growing_days_CF')
        Daily_Actual = request.POST.get('Daily_Actual')
        Month_day_01 = request.POST.get('Month_day_01')
        Month_day_02 = request.POST.get('Month_day_02')
        Month_day_03 = request.POST.get('Month_day_03')
        Month_day_04 = request.POST.get('Month_day_04')
        Month_day_05 = request.POST.get('Month_day_05')
        Month_day_06 = request.POST.get('Month_day_06')
        Month_day_07 = request.POST.get('Month_day_07')
        Month_day_08 = request.POST.get('Month_day_08')
        Month_day_09 = request.POST.get('Month_day_09')
        Month_day_10 = request.POST.get('Month_day_10')
        Month_day_11 = request.POST.get('Month_day_11')
        Month_day_12 = request.POST.get('Month_day_12')
        Month_day_13 = request.POST.get('Month_day_13')
        Month_day_14 = request.POST.get('Month_day_14')
        Month_day_15 = request.POST.get('Month_day_15')
        Month_day_16 = request.POST.get('Month_day_16')
        Month_day_17 = request.POST.get('Month_day_17')
        Month_day_18 = request.POST.get('Month_day_18')
        Month_day_19 = request.POST.get('Month_day_19')
        Month_day_20 = request.POST.get('Month_day_20')
        Month_day_21 = request.POST.get('Month_day_21')
        Month_day_22 = request.POST.get('Month_day_22')
        Month_day_23 = request.POST.get('Month_day_23')
        Month_day_24 = request.POST.get('Month_day_24')
        Month_day_25 = request.POST.get('Month_day_25')
        Month_day_26 = request.POST.get('Month_day_26')
        Month_day_27 = request.POST.get('Month_day_27')
        Month_day_28 = request.POST.get('Month_day_28')
        Month_day_29 = request.POST.get('Month_day_29')
        Month_day_30 = request.POST.get('Month_day_30')
        Month_day_31 = request.POST.get('Month_day_31')

        insert = TeaPluckingCycle(Zone=Zone, Fields=Fields,
                                  Growing_days_CF=Growing_days_CF, Daily_Actual=Daily_Actual, Month_day_01=Month_day_01,
                                  Month_day_02=Month_day_02, Month_day_03=Month_day_03, Month_day_04=Month_day_04,
                                  Month_day_05=Month_day_05, Month_day_06=Month_day_06, Month_day_07=Month_day_07,
                                  Month_day_08=Month_day_08, Month_day_09=Month_day_09, Month_day_10=Month_day_10,
                                  Month_day_11=Month_day_11, Month_day_12=Month_day_12, Month_day_13=Month_day_13,
                                  Month_day_14=Month_day_14, Month_day_15=Month_day_15, Month_day_16=Month_day_16,
                                  Month_day_17=Month_day_17, Month_day_18=Month_day_18, Month_day_19=Month_day_19,
                                  Month_day_20=Month_day_20, Month_day_21=Month_day_21, Month_day_22=Month_day_22,
                                  Month_day_23=Month_day_23, Month_day_24=Month_day_24, Month_day_25=Month_day_25,
                                  Month_day_26=Month_day_26, Month_day_27=Month_day_27, Month_day_28=Month_day_28,
                                  Month_day_29=Month_day_29, Month_day_30=Month_day_30, Month_day_31=Month_day_31)
        insert.save()

    return redirect('/plucking-cycle')


def TeaPluckingCycleEdit(request, pk):
    fields = TeaPluckingCycle.objects.get(id=pk)
    if request.method == 'POST':
        form = CycleForms(request.POST, instance=fields)
        if form.is_valid():
            form.save()
            return redirect('/plucking-cycle')

    else:
        form = CycleForms(instance=fields)

    context = {
        'form': form, 'CycleForms': CycleForms,

    }
    return render(request, 'Teapluckingcycle/update.html', context)


def TeaPluckingCycleDelete(request, pk):
    data = TeaPluckingCycle.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('/plucking-cycle')

    context = {
        'data': data,
    }
    return render(request, 'Teapluckingcycle/delete.html', context)
