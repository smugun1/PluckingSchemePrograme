def FieldsViewUpdate(request):
    data = FieldsToPluck.objects.all()
    field_data = {
        'Zone E': {
            'Field_No': ['5', '3', '7', '12', '14', '15'],
            'Leaf_Type': ['SD', 'SD', 'VP', 'VP', 'VP'],
            'Ha': [13.02, 8.27, 14.99, 12.93, 22.60, 10.65],
            'Days_to_Plk': [1, 2, 1, 2, 2, 1],
            'Prune_Age': [2, 2, 1, 0, 3, 4],
            'Num_of_Schemes': [185, 145, 92, 152, 323, 167],
            'Growing_Days_CF': [1, 2, 1, 2, 1, 0],
            'Month_days_Jan': [31, 31, 31, 31, 31, 31],
            'Month_days_Feb': [28, 28, 28, 28, 28, 28],
            'Month_days_Mar': [31, 31, 31, 31, 31, 31],
            'Month_days_Apr': [30, 30, 30, 30, 30, 30],
            'Month_days_May': [31, 31, 31, 31, 31, 31],
            'Month_days_Jun': [30, 30, 30, 30, 30, 30],
            'Month_days_Jul': [31, 31, 31, 31, 31, 31],
            'Month_days_Aug': [31, 31, 31, 31, 31, 31],
            'Month_days_Sep': [30, 30, 30, 30, 30, 30],
            'Month_days_Oct': [31, 31, 31, 31, 31, 31],
            'Month_days_Nov': [30, 30, 30, 30, 30, 30],
            'Month_days_Dec': [31, 31, 31, 31, 31, 31],
        },
        'Zone F': {
            'Field_No': ['11', '10', '42', '2', '6', '43'],
            'Leaf_Type': ['SD', 'SD', 'VP', 'SD', 'VP'],
            'Ha': [16.01, 22.55, 7.51, 7.41, 17.00, 4.6],
            'Days_to_Plk': [2, 3, 1, 1, 2, 1],
            'Prune_Age': [2, 1, 3, 1, 0, 1],
            'Num_of_Schemes': [178, 251, 107, 106, 189, 66],
            'Growing_Days_CF': [9, 3, 1, 3, 1, 2],
            'Month_days_Jan': [31, 31, 31, 31, 31, 31],
            'Month_days_Feb': [28, 28, 28, 28, 28, 28],
            'Month_days_Mar': [31, 31, 31, 31, 31, 31],
            'Month_days_Apr': [30, 30, 30, 30, 30, 30],
            'Month_days_May': [31, 31, 31, 31, 31, 31],
            'Month_days_Jun': [30, 30, 30, 30, 30, 30],
            'Month_days_Jul': [31, 31, 31, 31, 31, 31],
            'Month_days_Aug': [31, 31, 31, 31, 31, 31],
            'Month_days_Sep': [30, 30, 30, 30, 30, 30],
            'Month_days_Oct': [31, 31, 31, 31, 31, 31],
            'Month_days_Nov': [30, 30, 30, 30, 30, 30],
            'Month_days_Dec': [31, 31, 31, 31, 31, 31],
        },
        'Zone G': {
            'Field_No': ['8', '1', '44', '13', '9', '4'],
            'Leaf_Type': ['VP', 'SD', 'VP', 'VP', 'SD', 'VP'],
            'Ha': [9.07, 17.06, 7.19, 14.34, 20.43, 16.36],
            'Days_to_Plk': [1, 2, 1, 1, 2, 2],
            'Prune_Age': [3, 1, 2, 1, 3, 3],
            'Num_of_Schemes': [130, 190, 71, 113, 158, 165],
            'Growing_Days_CF': [1, 2, 1, 1, 2, 2],
            'Month_days_Jan': [31, 31, 31, 31, 31, 31],
            'Month_days_Feb': [28, 28, 28, 28, 28, 28],
            'Month_days_Mar': [31, 31, 31, 31, 31, 31],
            'Month_days_Apr': [30, 30, 30, 30, 30, 30],
            'Month_days_May': [31, 31, 31, 31, 31, 31],
            'Month_days_Jun': [30, 30, 30, 30, 30, 30],
            'Month_days_Jul': [31, 31, 31, 31, 31, 31],
            'Month_days_Aug': [31, 31, 31, 31, 31, 31],
            'Month_days_Sep': [30, 30, 30, 30, 30, 30],
            'Month_days_Oct': [31, 31, 31, 31, 31, 31],
            'Month_days_Nov': [30, 30, 30, 30, 30, 30],
            'Month_days_Dec': [31, 31, 31, 31, 31, 31],

        },
    }

    zone_list = ['Zone G', 'Zone F', 'Zone E']
    context = {}

    for zone in zone_list:
        field_index = int(Field_No) - 1
        if field_index < len(field_data[zone]['Field_No']):
            field_no = field_data[zone]['Field_No'][field_index]
            leaf_type = field_data[zone]['Leaf_Type'][field_index]
            ha = field_data[zone]['Ha'][field_index]
            days_to_plk = field_data[zone]['Days_to_Plk'][field_index]
            prune_age = field_data[zone]['Prune_Age'][field_index]
            num_of_schemes = field_data[zone]['Num_of_Schemes'][field_index]
            growing_days_cf = field_data[zone]['Growing_Days_CF'][field_index]
            month_days = {
                'Jan': field_data[zone]['Month_days_Jan'][field_index],
                'Feb': field_data[zone]['Month_days_Feb'][field_index],
                'Mar': field_data[zone]['Month_days_Mar'][field_index],
                # Include the remaining months here...
            }

            context[zone] = {
                'field_no': field_no,
                'leaf_type': leaf_type,
                'ha': ha,
                'days_to_plk': days_to_plk,
                'prune_age': prune_age,
                'num_of_schemes': num_of_schemes,
                'growing_days_cf': growing_days_cf,
                'month_days': month_days
            }

    return render(request, 'UpdateFields/psp_fields_rounds_checker-update.html', context)
