days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year1):
    if (year1 % 4) == 0:
        if (year1 % 100) == 0:
            if (year1 % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# We are going to iterate each month, but let's gat total days of each month
def total_days_per_month(year, month):
    if is_leap_year(year) and month == 2:
        return 29
    return days_month[month - 1]


def days_between_dates(year1, month1, day1, year2, month2, day2):
    days = 0
    while year1 < year2 or month1 < month2:
        days += total_days_per_month(year1, month1)
        month1 += 1
        if month1 == 13:
            year1 += 1
            month1 = 1

    return days - day1 + day2


def test():
    days_between_dates(1900, 1, 1, 1999, 12, 31)
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]
    for (args, answer) in test_cases:
        result = days_between_dates(*args)
        if result != answer:
            print("Test with data:", args, "failed")

        else:
            print("Test case passed!")


test()
