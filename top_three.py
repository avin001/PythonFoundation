def top_three(input_list):
    """
    Returns a list of the three largest elements from input_list in order from largest to smallest.
    If input_list has fewer than three elements, return input_list sorted largest to smallest.
    """
    # if len(input_list) < 3:
    #     return sorted(input_list, reverse = True)
    # else:
    #     sorted_list = sorted(input_list, reverse = True)
    #     return sorted_list[:3]

    # solution above (commented) can be written in one simple line as below:
    return sorted(input_list, reverse=True)[:3]


print(top_three([2, 3, 5, 6, 8, 4, 2, 1]))
