from datetime import datetime

from django.db.models import Count
from django.shortcuts import redirect

from PSP.plucking.models import GrowingCycle


class TeaPluckingCycle(models.Model):
    Zone = models.CharField(max_length=100)
    Fields = models.CharField(max_length=100)
    Growing_days_CF = ArrayField(models.IntegerField())
    Rounds_space = ArrayField(models.IntegerField())
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
        return self.Fields


class GrowingDays(models.Model):
    Zone = models.CharField(max_length=100)
    Fields = models.IntegerField()
    Growing_Days = ArrayField(models.IntegerField())
    Growing_Days_CF = ArrayField(models.IntegerField())
    CF = ArrayField(models.IntegerField())
    today_date = models.DateField(auto_now_add=True, blank=False, null=False)
    plucking_round = models.IntegerField()
    total_plucking_round = models.IntegerField()
    month_end = models.IntegerField()
    days_bf = models.IntegerField()
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
        return self.Fields

def TeaPluckingCycleViewRetrieve(request):
    def Create(cls, zone, fields, growing_days_cf, rounds_space):
        tea_plucking_cycle = cls(Zone=zone, Fields=fields)
        tea_plucking_cycle.Growing_days_CF = growing_days_cf
        tea_plucking_cycle.Rounds_space = rounds_space
        return tea_plucking_cycle

    # For Growing_days_CF
    growing_days_cf = [1, None, None, None, None, None, None, 7]
    n_growing_days_cf = growing_days_cf.count(None)
    step_growing_days_cf = (7 - 1) / (n_growing_days_cf + 1)

    current_value = 1
    for i in range(len(growing_days_cf)):
        if growing_days_cf[i] is None:
            current_value += step_growing_days_cf
            growing_days_cf[i] = round(current_value)

    # For Rounds_space
    rounds_space = [None, None, None, None, None, None, None, 7, None, None, None, None, None, None, None, None, None,
                    7, None, None, None, None, None, None, None, None, None, None, None]
    n_rounds_space = rounds_space.count(None)
    step_rounds_space = (7 - 7) / (n_rounds_space + 1)

    first_non_none = rounds_space.index(7)
    last_non_none = len(rounds_space) - rounds_space[::-1].index(7) - 1

    current_value = 7
    for i in range(len(rounds_space)):
        if rounds_space[i] is None:
            current_value -= step_rounds_space
            rounds_space[i] = round(current_value)

    table_data = [
        {
            'Zone': 'E',
            'Fields': '14',
            'Growing_days_CF': [8, 1, 2],
            'Rounds_space': [1, 2, None, None, None, None, None, None, 1, 2, None, None, None, None, None, None, 1, 2,
                             None, None, None, None, None, None, 1, 2, None, None, None, None, None, None]
        },
        {
            'Zone': 'E',
            'Fields': '15',
            'Growing_days_CF': [6, None, 3],
            'Rounds_space': [None, None, 3, None, None, None, None, None, None, None, None, 3, None, None, None, None,
                             None, None, None, None, None, None, 3, None, None, None, None, None, None, None]
        },
        {
            'Zone': 'E',
            'Fields': '5',
            'Growing_days_CF': [4, None, None, None, 4, 5],
            'Rounds_space': [None, None, None, 4, 5, None, None, None, None, None, None, None, 4, 5, None, None, None,
                             None, None, None, 4, 5, None, None, None, None, None, None, None, 4, 5, None]
        },
        {
            'Zone': 'E',
            'Fields': '3',
            'Growing_days_CF': [3, None, None, None, None, 6],
            'Rounds_space': [None, None, None, None, None, 6, None, None, None, None, None, None, None, None, 6, None,
                             None, None, None, None, None, None, 6, None, None, None, None, None, None, None, 6, None]
        },
        {
            'Zone': 'E',
            'Fields': '7',
            'Growing_days_CF': [3, None, None, None, None, 6, 7],
            'Rounds_space': [None, None, None, None, None, 6, 7, None, None, None, None, None, None, None, 6, 7, None,
                             None, None, None, None, None, 6, 7, None, None, None, None, None, None, 6, 7]
        },
        {
            'Zone': 'E',
            'Fields': '12',
            'Growing_days_CF': [1, None, None, None, None, None, None, 7],
            'Rounds_space': [None, None, None, None, None, None, 7, None, None, None, None, None, None, None, 7, None,
                             None, None, None, None, None, 7, None, None, None, None, None, None, None, 7, None]
        },
        {
            'Zone': 'F',
            'Fields': '10',
            'Growing_days_CF': [8, 1, 2],
            'Rounds_space': [1, 2, None, None, None, None, None, None, 1, 2, None, None, None, None, None, None, 1, 2,
                             None, None, None, None, None, None, 1, 2, None, None, None, None, None, None]
        },
        {
            'Zone': 'F',
            'Fields': '42',
            'Growing_days_CF': [6, None, None, 3],
            'Rounds_space': [None, None, 3, None, None, None, None, None, None, None, None, 3, None, None, None, None,
                             None, None, None, None, None, None, 3, None, None, None, None, None, None, None]
        },
        {
            'Zone': 'F',
            'Fields': '6',
            'Growing_days_CF': [4, None, None, None, 4, 5],
            'Rounds_space': [None, None, None, None, 4, 5, None, None, None, None, None, None, 4, 5, None, None, None,
                             None, 4, 5, None, None, None, None, 4, 5, None, None, None, None]
        },
        {
            'Zone': 'F',
            'Fields': '2',
            'Growing_days_CF': [3, None, None, None, None, None, 6],
            'Rounds_space': [None, None, None, None, None, None, 6, None, None, None, None, None, None, None, 6, None,
                             None, None, None, None, None, None, None, None, None, None, None, None, None]
        },
        {
            'Zone': 'F',
            'Fields': '43',
            'Growing_days_CF': [2, None, None, None, None, 6, 7],
            'Rounds_space': [None, None, None, None, None, 6, 7, None, None, None, None, None, None, None, None, 6, 7,
                             None, None, None, None, None, None, None, None, None, None, None, None, None]
        },
        {
            'Zone': 'F',
            'Fields': '11',
            'Growing_days_CF': [1, None, None, None, None, None, None, 7],
            'Rounds_space': [None, None, None, None, None, None, None, 7, None, None, None, None, None, None, None,
                             None, None, 7, None, None, None, None, None, None, None, None, None, None, None]
        },
        # Add the remaining data GrowingCycles here...
        {
            'Zone': 'G',
            'Fields': '4',
            'Growing_days_CF': [8, 1, 2],
            'Rounds_space': [1, 2, None, None, None, None, None, None, 1, 2, None, None, None, None, None, None, 1, 2,
                             None, None, None, None, None, None, 1, 2, None, None, None, None, None, None]
        },
        {
            'Zone': 'G',
            'Fields': '8',
            'Growing_days_CF': [6, None, None, 3],
            'Rounds_space': [None, None, 3, None, None, None, None, None, None, None, None, 3, None, None, None, None,
                             None, None, None, None, None, None, 3, None, None, None, None, None, None, None]
        },
        {
            'Zone': 'G',
            'Fields': '1',
            'Growing_days_CF': [4, None, None, None, 4, 5],
            'Rounds_space': [None, None, None, None, 4, 5, None, None, None, None, None, None, 4, 5, None, None, None,
                             None, 4, 5, None, None, None, None, 4, 5, None, None, None, None]
        },
        {
            'Zone': 'G',
            'Fields': '44',
            'Growing_days_CF': [3, None, None, None, None, None, 6],
            'Rounds_space': [None, None, None, None, None, None, 6, None, None, None, None, None, None, None, 6, None,
                             None, None, None, None, None, None, None, None, None, None, None, None, None]
        },
        {
            'Zone': 'G',
            'Fields': '13',
            'Growing_days_CF': [2, None, None, None, None, 6, 7],
            'Rounds_space': [None, None, None, None, None, 6, 7, None, None, None, None, None, None, None, None, 6, 7,
                             None, None, None, None, None, None, None, None, None, None, None, None, None]
        },
        {
            'Zone': 'G',
            'Fields': '9',
            'Growing_days_CF': [1, None, None, None, None, None, None, 7],
            'Rounds_space': [None, None, None, None, None, None, None, 7, None, None, None, None, None, None, None,
                             None, None, 7, None, None, None, None, None, None, None, None, None, None, None]
        }
    ]

    context = {

        'table_data': table_data,
    }

    return render(request, 'Plucking/tea_plucking_cycle.html', context)


def TeaPluckingCycleViewUpdate(request):
    if request.method == 'POST':
        zone = request.POST.get('Zone')
        fields = request.POST.get('Fields')
        growing_days_cf = request.POST.getlist('Growing_days_CF[]')
        rounds_space = request.POST.getlist('Rounds_space[]')

        # Algorithm to fill the missing values
        def create(zone, fields, growing_days_cf, rounds_space):
            tea_plucking_cycle = {
                'Zone': zone,
                'Fields': fields,
                'Growing_days_CF': growing_days_cf,
                'Rounds_space': rounds_space
            }
            return tea_plucking_cycle

        # For Growing_days_CF
        n_growing_days_cf = growing_days_cf.count('')
        step_growing_days_cf = (7 - 1) / (n_growing_days_cf + 1)

        current_value = 1
        for i in range(len(growing_days_cf)):
            if growing_days_cf[i] == '':
                current_value += step_growing_days_cf
                growing_days_cf[i] = str(round(current_value))

        # For Rounds_space
        n_rounds_space = rounds_space.count('')
        step_rounds_space = (7 - 7) / (n_rounds_space + 1)

        first_non_none = rounds_space.index('7')
        last_non_none = len(rounds_space) - rounds_space[::-1].index('7') - 1

        current_value = 7
        for i in range(len(rounds_space)):
            if rounds_space[i] == '':
                current_value -= step_rounds_space
                rounds_space[i] = str(round(current_value))

    table_data = []  # Default value for table_data
    table_data = [
        {
            'Zone': 'E',
            'Fields': '14',
            'Growing_days_CF': [8, 1, 2],
            'Rounds_space': [1, 2, None, None, None, None, None, None, 1, 2, None, None, None, None, None, None, 1, 2,
                             None, None, None, None, None, None, 1, 2, None, None, None, None, None, None]
        },
        {
            'Zone': 'E',
            'Fields': '15',
            'Growing_days_CF': [6, None, 3],
            'Rounds_space': [None, None, 3, None, None, None, None, None, None, None, None, 3, None, None, None, None,
                             None, None, None, None, None, None, 3, None, None, None, None, None, None, None]
        },
        {
            'Zone': 'E',
            'Fields': '5',
            'Growing_days_CF': [4, None, None, None, 4, 5],
            'Rounds_space': [None, None, None, 4, 5, None, None, None, None, None, None, None, 4, 5, None, None, None,
                             None, None, None, 4, 5, None, None, None, None, None, None, None, 4, 5, None]
        },
        {
            'Zone': 'E',
            'Fields': '3',
            'Growing_days_CF': [3, None, None, None, None, 6],
            'Rounds_space': [None, None, None, None, None, 6, None, None, None, None, None, None, None, None, 6, None,
                             None, None, None, None, None, None, 6, None, None, None, None, None, None, None, 6, None]
        },
        {
            'Zone': 'E',
            'Fields': '7',
            'Growing_days_CF': [3, None, None, None, None, 6, 7],
            'Rounds_space': [None, None, None, None, None, 6, 7, None, None, None, None, None, None, None, 6, 7, None,
                             None, None, None, None, None, 6, 7, None, None, None, None, None, None, 6, 7]
        },
        {
            'Zone': 'E',
            'Fields': '12',
            'Growing_days_CF': [1, None, None, None, None, None, None, 7],
            'Rounds_space': [None, None, None, None, None, None, 7, None, None, None, None, None, None, None, 7, None,
                             None, None, None, None, None, 7, None, None, None, None, None, None, None, 7, None]
        },
        {
            'Zone': 'F',
            'Fields': '10',
            'Growing_days_CF': [8, 1, 2],
            'Rounds_space': [1, 2, None, None, None, None, None, None, 1, 2, None, None, None, None, None, None, 1, 2,
                             None, None, None, None, None, None, 1, 2, None, None, None, None, None, None]
        },
        {
            'Zone': 'F',
            'Fields': '42',
            'Growing_days_CF': [6, None, None, 3],
            'Rounds_space': [None, None, 3, None, None, None, None, None, None, None, None, 3, None, None, None, None,
                             None, None, None, None, None, None, 3, None, None, None, None, None, None, None]
        },
        {
            'Zone': 'F',
            'Fields': '6',
            'Growing_days_CF': [4, None, None, None, 4, 5],
            'Rounds_space': [None, None, None, None, 4, 5, None, None, None, None, None, None, 4, 5, None, None, None,
                             None, 4, 5, None, None, None, None, 4, 5, None, None, None, None]
        },
        {
            'Zone': 'F',
            'Fields': '2',
            'Growing_days_CF': [3, None, None, None, None, None, 6],
            'Rounds_space': [None, None, None, None, None, None, 6, None, None, None, None, None, None, None, 6, None,
                             None, None, None, None, None, None, None, None, None, None, None, None, None]
        },
        {
            'Zone': 'F',
            'Fields': '43',
            'Growing_days_CF': [2, None, None, None, None, 6, 7],
            'Rounds_space': [None, None, None, None, None, 6, 7, None, None, None, None, None, None, None, None, 6, 7,
                             None, None, None, None, None, None, None, None, None, None, None, None, None]
        },
        {
            'Zone': 'F',
            'Fields': '11',
            'Growing_days_CF': [1, None, None, None, None, None, None, 7],
            'Rounds_space': [None, None, None, None, None, None, None, 7, None, None, None, None, None, None, None,
                             None, None, 7, None, None, None, None, None, None, None, None, None, None, None]
        },
        # Add the remaining data GrowingCycles here...
        {
            'Zone': 'G',
            'Fields': '4',
            'Growing_days_CF': [8, 1, 2],
            'Rounds_space': [1, 2, None, None, None, None, None, None, 1, 2, None, None, None, None, None, None, 1, 2,
                             None, None, None, None, None, None, 1, 2, None, None, None, None, None, None]
        },
        {
            'Zone': 'G',
            'Fields': '8',
            'Growing_days_CF': [6, None, None, 3],
            'Rounds_space': [None, None, 3, None, None, None, None, None, None, None, None, 3, None, None, None, None,
                             None, None, None, None, None, None, 3, None, None, None, None, None, None, None]
        },
        {
            'Zone': 'G',
            'Fields': '1',
            'Growing_days_CF': [4, None, None, None, 4, 5],
            'Rounds_space': [None, None, None, None, 4, 5, None, None, None, None, None, None, 4, 5, None, None, None,
                             None, 4, 5, None, None, None, None, 4, 5, None, None, None, None]
        },
        {
            'Zone': 'G',
            'Fields': '44',
            'Growing_days_CF': [3, None, None, None, None, None, 6],
            'Rounds_space': [None, None, None, None, None, None, 6, None, None, None, None, None, None, None, 6, None,
                             None, None, None, None, None, None, None, None, None, None, None, None, None]
        },
        {
            'Zone': 'G',
            'Fields': '13',
            'Growing_days_CF': [2, None, None, None, None, 6, 7],
            'Rounds_space': [None, None, None, None, None, 6, 7, None, None, None, None, None, None, None, None, 6, 7,
                             None, None, None, None, None, None, None, None, None, None, None, None, None]
        },
        {
            'Zone': 'G',
            'Fields': '9',
            'Growing_days_CF': [1, None, None, None, None, None, None, 7],
            'Rounds_space': [None, None, None, None, None, None, None, 7, None, None, None, None, None, None, None,
                             None, None, 7, None, None, None, None, None, None, None, None, None, None, None]
        }
    ]
    if request.method == 'POST':
        # Retrieve the updated values from the request
        updated_data = {
            'Zone': request.POST.get('Zone'),
            'Fields': request.POST.get('Fields'),
            'Growing_days_CF': [int(day) if day else None for day in request.POST.getlist('Growing_days_CF')],
            'Rounds_space': [int(actual) if actual else None for actual in request.POST.getlist('Rounds_space')],
        }

        # Update the existing data with the updated values
        for i, data in enumerate(table_data):
            if i < len(updated_data):
                updated_GrowingCycle = updated_data[i]
                data['Growing_days_CF'] = updated_GrowingCycle.get('Growing_days_CF', data['Growing_days_CF'])
                data['Rounds_space'] = updated_GrowingCycle.get('Rounds_space', data['Rounds_space'])

        # Perform any necessary validation or database updates here

        context = {
            'table_data': table_data,
        }

        return render(request, 'Plucking/tea_plucking_cycle.html', context)

    else:
        context = {
            'table_data': [],  # Empty initial data
        }

        return render(request, 'Plucking/tea_plucking_cycle_update.html', context)


def TeaPluckingCycleViewCreate(request):
    if request.method == "POST":
        try:
            Zone = request.POST.get('Zone')
            Fields = request.POST.get('Fields')
            Growing_days_CF = request.POST.getlist('Growing_days_CF[]')
            Rounds_space = request.POST.getlist('Rounds_space[]')

            month_days = {}
            for i in range(1, 32):
                month_day = request.POST.get(f"Month_day_{i}")
                month_days[f"Month_day_{i:02d}"] = month_day

            insert = TeaPluckingCycle(
                Zone=Zone,
                Fields=Fields,
                Growing_days_CF=','.join(Growing_days_CF),
                Rounds_space=','.join(Rounds_space),
                **month_days
            )
            insert.save()

        except OperationalError as e:
            return render(request, 'error.html', {'error_message': str(e)})

        return redirect('/plucking-cycle')

    return render(request, 'plucking/tea_plucking_cycle.html')


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


def GrowingDaysViewRetrieve(request):
    if request.method == 'POST':
        # Process the submitted data
        data = request.POST.get('GrowingCycles_data', '').split('\n')

        # Parse the submitted data and create GrowingCycles accordingly
        zone = None
        for line in data:
            line = line.strip()
            if line:
                if line.startswith('Fields'):
                    # Extract the zone from the line
                    zone = line.split('\t')[0]
                else:
                    # Extract field data from the line
                    fields = line.split('\t')
                    field = int(fields[0])
                    growing_days = [int(x) for x in fields[1].split() if x.isdigit()]
                    cf_values = [int(x) if x.isdigit() else None for x in fields[2:]]

                    # Create GrowingCycles for each CF value
                    for i, cf in enumerate(cf_values, start=1):
                        if cf is not None:
                            date = request.POST.get('start_date')
                            date = datetime.strptime(date, '%Y-%m-%d') + timedelta(days=(i - 1) * 8)
                            balance = cf * i
                            GrowingCycle.objects.create(zone=zone, field=field, growing_days=growing_days[i - 1], cf=cf,
                                                        date=date, balance=balance)

        return redirect('growing-days')

    return render(request, 'Plucking/growing_days.html')


def GrowingDaysViewUpdate(request):
    data = None  # Initialize the variable with a default value
    if request.method == "POST":
        # Handle the POST request data
        data = request.POST.get('data')
    current_date = datetime.strptime("2023-05-01T20:16", "%Y-%m-%dT%H:%M")
    rd_today_date = datetime.strptime("2023-05-01T20:16", "%Y-%m-%dT%H:%M")  # round_today_date
    plucking_round = 8
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

    total_plucking_round = GrowingCycle.objects.aggregate(count=Count('plucking_round'))['count']
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
    Growing_Days_CF = month_end.day - (total_plucking_round * 8)
    if Growing_Days_CF <= month_end.day:
        Growing_Days_CF = 0
    else:
        Growing_Days_CF = month_end.day - (total_plucking_round * 8)
    today_date = datetime.today().date()
    n = month_end.date() - today_date
    months = int(n.days / 30)
    Growing_Days = month_end.day - (total_plucking_round * 8)
    if Growing_Days <= 0:
        Growing_Days = 0
    days_bf = (month_end.day - (total_plucking_round * 8))
    if days_bf >= 0:
        if (total_plucking_round * 8) >= 8 or 16 or 24:
            days_bf = days_bf % 8

    context = {
        "data": data,
        "rd_today_date": today_date,
        "plucking_round": plucking_round,
        "plucking_day": plucking_day,
        "next_plucking": next_plucking,
        "actual_plucking_day": actual_plucking_day,
        "total_plucking_round": total_plucking_round,
        "month_end": month_end,
        "Growing_Days_CF": Growing_Days_CF,
        "Growing_Days": Growing_Days,
        "days_bf": days_bf,
    }

    return render(request, 'Plucking/growing_days_update.html', context)


def GrowingDaysViewCreate(request):
    if request.method == "POST":
        try:
            Zone = request.POST.get('Zone')
            Fields = request.POST.get('Fields')
            Growing_days = request.POST.getlist('Growing_days[]')
            CF = request.POST.getlist('CF[]')
            today_date = request.GET.get('today_date') or None
            plucking_round = request.POST.get('plucking_round')
            plucking_day = request.GET.get('Plucking_day') or None
            next_plucking = request.GET.get('next_plucking') or None
            actual_plucking_day = request.GET.get('actual_plucking_day') or None
            total_plucking_round = request.POST.get('total_plucking_round')
            month_end = request.POST.get('month_end')
            Growing_Days_CF = request.POST.get('Growing_Days_CF')
            Growing_Days = request.POST.get('Growing_Days')
            days_bf = request.POST.get('days_bf')

            month_days = {}
            for i in range(1, 32):
                month_day = request.POST.get(f"Month_day_{i}")
                month_days[f"Month_day_{i:02d}"] = month_day

            insert = Growing_Days(
                Zone=Zone,
                Fields=Fields,
                Growing_days=','.join(Growing_days),
                CF=','.join(CF),
                **month_days,
                today_date=today_date,
                plucking_round=plucking_round,
                plucking_day=plucking_day,
                next_plucking=next_plucking,
                actual_plucking_day=actual_plucking_day,
                total_plucking_round=total_plucking_round,
                month_end=month_end,
                Growing_Days_CF=Growing_Days_CF,
                Growing_Days=Growing_Days,
                days_bf=days_bf,
            )
            insert.save()

        except OperationalError as e:
            return render(request, 'error.html', {'error_message': str(e)})

        return redirect('/growing-days')

    return render(request, 'plucking/growing_days.html')

    path('plucking-cycle/', views.TeaPluckingCycleViewRetrieve, name='plucking-cycle'),
    path('plucking-cycle-update/', views.TeaPluckingCycleViewUpdate, name='plucking-cycle-update'),
    path('plucking-cycle-create/', views.TeaPluckingCycleViewCreate, name='plucking-cycle-create'),

    path('growing-days/', views.GrowingDaysViewRetrieve, name='growing-days'),
    path('growing-days-update/', views.GrowingDaysViewUpdate, name='growing-days-update'),
    path('growing-days-create/', views.GrowingDaysViewCreate, name='growing-days-create'),

    path('teapluckingcycle-edit/<int:pk>/', views.TeaPluckingCycleEdit, name='teapluckingcycle-edit'),
    path('teapluckingcycle-delete/<int:pk>/', views.TeaPluckingCycleDelete, name='teapluckingcycle-delete'),