"""
A regular flying circus happens twice or three times a month. For each month, information about the amount of money taken at each event is saved in a list, so that the amounts appear in the order in which they happened. The months' data is all collected in a dictionary called monthly_takings.

For this quiz, write a function total_takings that calculates the sum of takings from every circus in the year.
"""

monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49], 'April': [57, 42], 'May': [55, 37], 'June': [34, 32], 'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62], 'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}


def total_takings(yearly_record):
    sum_of_all_takings_in_year = 0
    for record in yearly_record:
        monthly_takings_list = monthly_takings[record]
        sum_of_monthly_takings = 0
        for taking in monthly_takings_list:
            sum_of_monthly_takings += taking
        sum_of_all_takings_in_year += sum_of_monthly_takings
    return sum_of_all_takings_in_year


print(total_takings(monthly_takings))
