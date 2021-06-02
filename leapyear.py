def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year %100 == 0:
            return False
        leap = True


    return leap
