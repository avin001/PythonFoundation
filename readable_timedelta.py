def readable_timedelta(days):
    """Calculate the number of weeks and days contained in given number of days

    days: int. Given number of days
    Function readable_timedelta(10) returns string: 1 week(s) and 3 day(s).
    """
    number_of_weeks = days // 7
    remainder_days = days % 7
    return "{} week(s) and {} day(s)".format(number_of_weeks, remainder_days)


print(readable_timedelta(10))
