# from calendar import month
#
# from django.db.models import Sum
#
#
# def rounds_monitor_retrieve(request):
#     data = RoundsMonitor.objects.all()
#     today_date = datetime.date.today()
#     plucking_round = 8
#     plucking_day = today_date + datetime.timedelta(days=plucking_round)
#     next_plucking = plucking_day + datetime.timedelta(days=plucking_round)
#     actual_plucking_day = today_date + datetime.timedelta(days=plucking_round)
#     days_behind = plucking_day - actual_plucking_day
#     days_ahead = actual_plucking_day - plucking_round
#     total_plucking_round = RoundsMonitor.objects.aggregate(Sum('plucking_round'))['plucking_round__sum']
#     month_end = today_date.replace(day=1, month=today_date.month + 1, day=1) - datetime.timedelta(days=1)
#     if today_date.month == 2:
#         if today_date.year % 4 == 0 and (today_date.year % 100 != 0 or today_date.year % 400 == 0):
#             month_end = month_end.replace(day=29)
#         else:
#             month_end = month_end.replace(day=28)
#     elif today_date.month in [1, 3, 5, 7, 8, 10, 12]:
#         month_end = month_end.replace(day=31)
#     else:
#         month_end = month_end.replace(day=30)
#     round_bal_days = month_end.day - total_plucking_round
#     days_to_end_month = month_end.day - round_bal_days
#     days_bf = days_to_end_month - round_bal_days
