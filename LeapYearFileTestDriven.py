def LeapYear(yearIn):
    year = int(yearIn)
    if(year%100==0 and year%400!=0):
        print(str(year) +" is not a leap year")
        return False
print(LeapYear(1700))