
def leap_year(year):
    if year % 400 == 0:
        print("Leap year")
    else:
        if year % 4 == 0 and year % 100 != 0:
            print("leap year")
        else:
            print("Not a leap year")


leap_year(1980)
