#

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        return 29
    return month_days[month - 1]

def day_of_year(year, month, day):
    days = days_in_month(year, month)
    if days is None or day < 1 or day > days:
        return None

    return sum(days_in_month(year, current_month) for current_month in range(1, month)) + day

print(day_of_year(2000, 12, 31))
