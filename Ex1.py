def enter_date(date):
    date_list = date.split(".")
    if len(date_list) != 3:
        print("Too many or too less values!")
        return "null"
    else:
        day, month, year = date.split(".")
        try:
            day = int(day)
            month = int(month)
            year = int(year)
            return date
        except:
            print("Date must consist of numbers!")
            return "null"


def _leapyear_check(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


def check_date(date):
    day, month, year = date.split(".")
    day = int(day)
    month = int(month)
    year = int(year)
    leap_check = _leapyear_check(year)
    if 0 < year < 10000:
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if 0 < day < 32:
                return True
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if 0 < day < 31:
                return True
        elif month == 2:
            if 0 < day < 30 and leap_check:
                return True
            elif 0 < day < 29:
                return True
    return False


date = input("Enter your date in DD.MM.YYYY format:")
date = enter_date(date)
if date != "null":
    print(check_date(date))
