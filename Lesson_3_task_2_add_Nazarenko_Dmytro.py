# task add # 2

while True:
    year = int (input("enter year number or type -1 to exit : "))
    if year == -1: 
        break
    elif year < 1582:
        print ("Not within the Gregorian calendar period")
    elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print ("The year is leap")
    else: 
        print ("The year is not leap")
