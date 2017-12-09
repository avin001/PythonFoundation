# Write a function that uses a tuple to return multiple values. Write an hours2days function that takes one argument, an integer, that is a time period in hours. The function should return a tuple of how long that period is in days and hours, with hours being the remainder that can't be expressed in days. For example, 39 hours is 1 day and 15 hours, so the function should return (1,15).


def hours2days(time_period_in_hours):
    days, hours = time_period_in_hours // 24, time_period_in_hours % 24
    return days, hours


print(hours2days(50))
