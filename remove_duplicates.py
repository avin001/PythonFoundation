def remove_duplicates(input_list):
    unique_list = []
    for list_item in input_list:
        if list_item not in unique_list:
            unique_list.append(list_item)
    return unique_list


print(remove_duplicates(['aquarius', 'pisces', 'libra', 'aquarius', 'pisces']))
