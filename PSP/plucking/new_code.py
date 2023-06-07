# AutoFieldsViewRetrieve(request):
#  # Retrieve field data from the database
#     data = AutoFields.objects.all()
#
#     Division_data = {
#         'Zone E': {
#             'Field_No': ['5', '3', '7', '12', '14', '15'],
#             'Leaf_Type': ['SD', 'SD', 'VP', 'VP', 'VP'],
#             'Ha': [13.02, 8.27, 14.99, 12.93, 22.60, 10.65],
#             'Days_to_plk': [1, 2, 1, 2, 2, 1],
#             'Prune_age': [2, 2, 1, 0, 3, 4],
#             'Num_of_Schemes': [185, 145, 92, 152, 323, 167],
#             'Growing_days_CF': [1, 2, 1, 2, 1, 0],
#             'Month_day_Jan': [31, 31, 31, 31, 31, 31],
#             'Month_day_Feb': [28, 28, 28, 28, 28, 28],
#             'Month_day_Mar': [31, 31, 31, 31, 31, 31],
#             'Month_day_Apr': [30, 30, 30, 30, 30, 30],
#             'Month_day_May': [31, 31, 31, 31, 31, 31],
#             'Month_day_Jun': [30, 30, 30, 30, 30, 30],
#             'Month_day_Jul': [31, 31, 31, 31, 31, 31],
#             'Month_day_Aug': [31, 31, 31, 31, 31, 31],
#             'Month_day_Sep': [30, 30, 30, 30, 30, 30],
#             'Month_day_Oct': [31, 31, 31, 31, 31, 31],
#             'Month_day_Nov': [30, 30, 30, 30, 30, 30],
#             'Month_day_Dec': [31, 31, 31, 31, 31, 31],
#         },
#         'Zone F': {
#             'Field_No': ['11', '10', '42', '2', '6', '43'],
#             'Leaf_Type': ['SD', 'SD', 'VP', 'SD', 'VP'],
#             'Ha': [16.01, 22.55, 7.51, 7.41, 17.00, 4.6],
#             'Days_to_plk': [2, 3, 1, 1, 2, 1],
#             'Prune_age': [2, 1, 3, 1, 0, 1],
#             'Num_of_Schemes': [178, 251, 107, 106, 189, 66],
#             'Growing_days_CF': [9, 3, 1, 3, 1, 2],
#             'Month_day_Jan': [31, 31, 31, 31, 31, 31],
#             'Month_day_Feb': [28, 28, 28, 28, 28, 28],
#             'Month_day_Mar': [31, 31, 31, 31, 31, 31],
#             'Month_day_Apr': [30, 30, 30, 30, 30, 30],
#             'Month_day_May': [31, 31, 31, 31, 31, 31],
#             'Month_day_Jun': [30, 30, 30, 30, 30, 30],
#             'Month_day_Jul': [31, 31, 31, 31, 31, 31],
#             'Month_day_Aug': [31, 31, 31, 31, 31, 31],
#             'Month_day_Sep': [30, 30, 30, 30, 30, 30],
#             'Month_day_Oct': [31, 31, 31, 31, 31, 31],
#             'Month_day_Nov': [30, 30, 30, 30, 30, 30],
#             'Month_day_Dec': [31, 31, 31, 31, 31, 31],
#         },
#         'Zone G': {
#             'Field_No': ['8', '1', '44', '13', '9', '4'],
#             'Leaf_Type': ['VP', 'SD', 'VP', 'VP', 'SD', 'VP'],
#             'Ha': [9.07, 17.06, 7.19, 14.34, 20.43, 16.36],
#             'Days_to_plk': [1, 2, 1, 1, 2, 2],
#             'Prune_age': [3, 1, 2, 1, 3, 3],
#             'Num_of_Schemes': [130, 190, 71, 113, 158, 165],
#             'Growing_days_CF': [1, 2, 1, 1, 2, 2],
#             'Month_day_Jan': [31, 31, 31, 31, 31, 31],
#             'Month_day_Feb': [28, 28, 28, 28, 28, 28],
#             'Month_day_Mar': [31, 31, 31, 31, 31, 31],
#             'Month_day_Apr': [30, 30, 30, 30, 30, 30],
#             'Month_day_May': [31, 31, 31, 31, 31, 31],
#             'Month_day_Jun': [30, 30, 30, 30, 30, 30],
#             'Month_day_Jul': [31, 31, 31, 31, 31, 31],
#             'Month_day_Aug': [31, 31, 31, 31, 31, 31],
#             'Month_day_Sep': [30, 30, 30, 30, 30, 30],
#             'Month_day_Oct': [31, 31, 31, 31, 31, 31],
#             'Month_day_Nov': [30, 30, 30, 30, 30, 30],
#             'Month_day_Dec': [31, 31, 31, 31, 31, 31],
#
#         },
#     }
#
#     Division_data_list = []
#
#     for Division, zone_data in Division_data.items():
#         field_indexes = []
#         for field_no in zone_data['Field_No']:
#             field_index = next(
#                 (index for index, field in enumerate(data) if field.Field_No == field_no), None)
#             if field_index is not None:
#                 field_indexes.append(field_index)
#
#         for field_index in field_indexes:
#             Division_data_list.append({
#                 'Field_No': zone_data['Field_No'][field_index],
#                 'Leaf_Type': zone_data['Leaf_Type'][field_index],
#                 'Ha': zone_data['Ha'][field_index],
#                 'Days_to_plk': zone_data['Days_to_plk'][field_index],
#                 'Prune_age': zone_data['Prune_age'][field_index],
#                 'Num_of_Schemes': zone_data['Num_of_Schemes'][field_index],
#                 'Growing_days_CF': zone_data['Growing_days_CF'][field_index],
#                 'Month_day_Jan': zone_data['Month_day_Jan'][field_index],
#                 'Month_day_Feb': zone_data['Month_day_Feb'][field_index],
#                 'Month_day_Mar': zone_data['Month_day_Mar'][field_index],
#                 'Month_day_Apr': zone_data['Month_day_Apr'][field_index],
#                 'Month_day_May': zone_data['Month_day_May'][field_index],
#                 'Month_day_Jun': zone_data['Month_day_Jun'][field_index],
#                 'Month_day_Jul': zone_data['Month_day_Jul'][field_index],
#                 'Month_day_Aug': zone_data['Month_day_Aug'][field_index],
#                 'Month_day_Sep': zone_data['Month_day_Sep'][field_index],
#                 'Month_day_Oct': zone_data['Month_day_Oct'][field_index],
#                 'Month_day_Nov': zone_data['Month_day_Nov'][field_index],
#                 'Month_day_Dec': zone_data['Month_day_Dec'][field_index]
#             })
#
#     month = 5
#     num_days = {
#         1: 31,
#         2: 28,
#         3: 31,
#         4: 30,
#         5: 31,
#         6: 30,
#         7: 31,
#         8: 31,
#         9: 30,
#         10: 31,
#         11: 30,
#         12: 31
#     }
#
#     context = {
#         'autofields': data,
#         'Division_data': Division_data_list,
#         'num_days': num_days[month]
#     }
#
#     return render(request, 'Plucking/autofields_psp.html', context)
#
#
# def AutoFieldsViewUpdate(request):
#     data = AutoFields.objects.all()
#     Division_data = {
#         'Zone E': {
#             'Field_No': ['5', '3', '7', '12', '14', '15'],
#             'Leaf_Type': ['SD', 'SD', 'VP', 'VP', 'VP'],
#             'Ha': [13.02, 8.27, 14.99, 12.93, 22.60, 10.65],
#             'Days_to_plk': [1, 2, 1, 2, 2, 1],
#             'Prune_age': [2, 2, 1, 0, 3, 4],
#             'Num_of_Schemes': [185, 145, 92, 152, 323, 167],
#             'Growing_days_CF': [1, 2, 1, 2, 1, 0],
#             'Month_day_Jan': [31, 31, 31, 31, 31, 31],
#             'Month_day_Feb': [28, 28, 28, 28, 28, 28],
#             'Month_day_Mar': [31, 31, 31, 31, 31, 31],
#             'Month_day_Apr': [30, 30, 30, 30, 30, 30],
#             'Month_day_May': [31, 31, 31, 31, 31, 31],
#             'Month_day_Jun': [30, 30, 30, 30, 30, 30],
#             'Month_day_Jul': [31, 31, 31, 31, 31, 31],
#             'Month_day_Aug': [31, 31, 31, 31, 31, 31],
#             'Month_day_Sep': [30, 30, 30, 30, 30, 30],
#             'Month_day_Oct': [31, 31, 31, 31, 31, 31],
#             'Month_day_Nov': [30, 30, 30, 30, 30, 30],
#             'Month_day_Dec': [31, 31, 31, 31, 31, 31],
#         },
#         'Zone F': {
#             'Field_No': ['11', '10', '42', '2', '6', '43'],
#             'Leaf_Type': ['SD', 'SD', 'VP', 'SD', 'VP'],
#             'Ha': [16.01, 22.55, 7.51, 7.41, 17.00, 4.6],
#             'Days_to_plk': [2, 3, 1, 1, 2, 1],
#             'Prune_age': [2, 1, 3, 1, 0, 1],
#             'Num_of_Schemes': [178, 251, 107, 106, 189, 66],
#             'Growing_days_CF': [9, 3, 1, 3, 1, 2],
#             'Month_day_Jan': [31, 31, 31, 31, 31, 31],
#             'Month_day_Feb': [28, 28, 28, 28, 28, 28],
#             'Month_day_Mar': [31, 31, 31, 31, 31, 31],
#             'Month_day_Apr': [30, 30, 30, 30, 30, 30],
#             'Month_day_May': [31, 31, 31, 31, 31, 31],
#             'Month_day_Jun': [30, 30, 30, 30, 30, 30],
#             'Month_day_Jul': [31, 31, 31, 31, 31, 31],
#             'Month_day_Aug': [31, 31, 31, 31, 31, 31],
#             'Month_day_Sep': [30, 30, 30, 30, 30, 30],
#             'Month_day_Oct': [31, 31, 31, 31, 31, 31],
#             'Month_day_Nov': [30, 30, 30, 30, 30, 30],
#             'Month_day_Dec': [31, 31, 31, 31, 31, 31],
#         },
#         'Zone G': {
#             'Field_No': ['8', '1', '44', '13', '9', '4'],
#             'Leaf_Type': ['VP', 'SD', 'VP', 'VP', 'SD', 'VP'],
#             'Ha': [9.07, 17.06, 7.19, 14.34, 20.43, 16.36],
#             'Days_to_plk': [1, 2, 1, 1, 2, 2],
#             'Prune_age': [3, 1, 2, 1, 3, 3],
#             'Num_of_Schemes': [130, 190, 71, 113, 158, 165],
#             'Growing_days_CF': [1, 2, 1, 1, 2, 2],
#             'Month_day_Jan': [31, 31, 31, 31, 31, 31],
#             'Month_day_Feb': [28, 28, 28, 28, 28, 28],
#             'Month_day_Mar': [31, 31, 31, 31, 31, 31],
#             'Month_day_Apr': [30, 30, 30, 30, 30, 30],
#             'Month_day_May': [31, 31, 31, 31, 31, 31],
#             'Month_day_Jun': [30, 30, 30, 30, 30, 30],
#             'Month_day_Jul': [31, 31, 31, 31, 31, 31],
#             'Month_day_Aug': [31, 31, 31, 31, 31, 31],
#             'Month_day_Sep': [30, 30, 30, 30, 30, 30],
#             'Month_day_Oct': [31, 31, 31, 31, 31, 31],
#             'Month_day_Nov': [30, 30, 30, 30, 30, 30],
#             'Month_day_Dec': [31, 31, 31, 31, 31, 31],
#
#         },
#     }
#
#     if data:
#         zone = data[0].Zone
#     else:
#         zone = None
#
#     if request.method == 'POST':
#         Field_No = request.POST.get('Field_No')  # Retrieve Field_No from POST request
#     else:
#         Field_No = request.GET.get('Field_No')  # Retrieve Field_No from GET request
#
#     if Field_No is not None:
#         field_index = int(Field_No) - 1
#     else:
#         field_index = None
#
#     zone_data = Division_data.get(zone, {})
#     Division_data = {
#         'Zone': zone_data.get('Zone', []),
#         'Leaf_Type': zone_data.get('Leaf_Type', []),
#         'Ha': zone_data.get('Ha', []),
#         'Days_to_plk': zone_data.get('Days_to_plk', []),
#         'Prune_age': zone_data.get('Prune_age', []),
#         'Num_of_Schemes': zone_data.get('Num_of_Schemes', []),
#         'Growing_days_CF': zone_data.get('Growing_days_CF', []),
#         'Month_day_Jan': zone_data.get('Month_day_Jan', []),
#         'Month_day_Feb': zone_data.get('Month_day_Feb', []),
#         'Month_day_Mar': zone_data.get('Month_day_Mar', []),
#         'Month_day_Apr': zone_data.get('Month_day_Apr', []),
#         'Month_day_May': zone_data.get('Month_day_May', []),
#         'Month_day_Jun': zone_data.get('Month_day_Jun', []),
#         'Month_day_Jul': zone_data.get('Month_day_Jul', []),
#         'Month_day_Aug': zone_data.get('Month_day_Aug', []),
#         'Month_day_Sep': zone_data.get('Month_day_Sep', []),
#         'Month_day_Oct': zone_data.get('Month_day_Oct', []),
#         'Month_day_Nov': zone_data.get('Month_day_Nov', []),
#         'Month_day_Dec': zone_data.get('Month_day_Dec', []),
#     }
#
#     return render(request, 'Plucking/autofields_psp_update.html', {'Division_data': Division_data})
#
#
# def AutoFieldsViewCreate(request):
#     if request.method == "POST":
#         Zone = request.POST.get('Zone')
#         Field_No = request.POST.get('Field_No')
#         Leaf_Type = request.POST.get('Leaf_Type')
#         Ha = request.POST.get('Ha')
#         Days_to_plk = request.POST.get('Days_to_plk')
#         Prune_age = request.POST.get('Prune_age')
#         Number_of_schemes = request.POST.get('Number_of_schemes')
#         Growing_days_CF = request.POST.get('Growing_days_CF')
#         Month_day_01 = request.POST.get('Month_day_01')
#         Month_day_02 = request.POST.get('Month_day_02')
#         Month_day_03 = request.POST.get('Month_day_03')
#         Month_day_04 = request.POST.get('Month_day_04')
#         Month_day_05 = request.POST.get('Month_day_05')
#         Month_day_06 = request.POST.get('Month_day_06')
#         Month_day_07 = request.POST.get('Month_day_07')
#         Month_day_08 = request.POST.get('Month_day_08')
#         Month_day_09 = request.POST.get('Month_day_09')
#         Month_day_10 = request.POST.get('Month_day_10')
#         Month_day_11 = request.POST.get('Month_day_11')
#         Month_day_12 = request.POST.get('Month_day_12')
#         Month_day_13 = request.POST.get('Month_day_13')
#         Month_day_14 = request.POST.get('Month_day_14')
#         Month_day_15 = request.POST.get('Month_day_15')
#         Month_day_16 = request.POST.get('Month_day_16')
#         Month_day_17 = request.POST.get('Month_day_17')
#         Month_day_18 = request.POST.get('Month_day_18')
#         Month_day_19 = request.POST.get('Month_day_19')
#         Month_day_20 = request.POST.get('Month_day_20')
#         Month_day_21 = request.POST.get('Month_day_21')
#         Month_day_22 = request.POST.get('Month_day_22')
#         Month_day_23 = request.POST.get('Month_day_23')
#         Month_day_24 = request.POST.get('Month_day_24')
#         Month_day_25 = request.POST.get('Month_day_25')
#         Month_day_26 = request.POST.get('Month_day_26')
#         Month_day_27 = request.POST.get('Month_day_27')
#         Month_day_28 = request.POST.get('Month_day_28')
#         Month_day_29 = request.POST.get('Month_day_29')
#         Month_day_30 = request.POST.get('Month_day_30')
#         Month_day_31 = request.POST.get('Month_day_31')
#
#         insert = AutoFields(Zone=Zone, Field_No=Field_No, Leaf_Type=Leaf_Type, Ha=Ha, Days_to_plk=Days_to_plk,
#                                Prune_age=Prune_age, Number_of_schemes=Number_of_schemes,
#                                Growing_days_CF=Growing_days_CF, Month_day_01=Month_day_01,
#                                Month_day_02=Month_day_02, Month_day_03=Month_day_03, Month_day_04=Month_day_04,
#                                Month_day_05=Month_day_05, Month_day_06=Month_day_06, Month_day_07=Month_day_07,
#                                Month_day_08=Month_day_08, Month_day_09=Month_day_09, Month_day_10=Month_day_10,
#                                Month_day_11=Month_day_11, Month_day_12=Month_day_12, Month_day_13=Month_day_13,
#                                Month_day_14=Month_day_14, Month_day_15=Month_day_15, Month_day_16=Month_day_16,
#                                Month_day_17=Month_day_17, Month_day_18=Month_day_18, Month_day_19=Month_day_19,
#                                Month_day_20=Month_day_20, Month_day_21=Month_day_21, Month_day_22=Month_day_22,
#                                Month_day_23=Month_day_23, Month_day_24=Month_day_24, Month_day_25=Month_day_25,
#                                Month_day_26=Month_day_26, Month_day_27=Month_day_27, Month_day_28=Month_day_28,
#                                Month_day_29=Month_day_29, Month_day_30=Month_day_30, Month_day_31=Month_day_31)
#         insert.save()
#
#     return redirect('/autofields-record')
#
#
# def AutoFieldsEdit(request, pk):
#     fields = AutoFields.objects.get(id=pk)
#     if request.method == 'POST':
#         form = FieldsForms(request.POST, instance=fields)
#         if form.is_valid():
#             form.save()
#             return redirect('/autofields-record')
#
#     else:
#         form = FieldsForms(instance=fields)
#
#     context = {
#         'form': form, 'FieldsForms': FieldsForms,
#
#     }
#     return render(request, 'Autofields/update.html', context)
#
#
# def AutoFieldsDelete(request, pk):
#     data = AutoFields.objects.get(id=pk)
#     if request.method == 'POST':
#         data.delete()
#         return redirect('/autofields-record')
#
#     context = {
#         'data': data,
#     }
#     return render(request, 'Autofields/delete.html', context)