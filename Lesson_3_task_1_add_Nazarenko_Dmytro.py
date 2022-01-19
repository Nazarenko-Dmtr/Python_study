# task add # 1

while True:
    flat_number = int (input("insert flat number: "))
    entrance_number = flat_number // 36 + 1
    if 0 > flat_number < 144:
        if flat_number % 4 == 0 and flat_number // 4 < 9:
            floor_number = int (flat_number / 4)
        elif flat_number % 4 == 0 and flat_number // 4 > 9:
            floor_number = int (flat_number // 4 - 9)
        else:
            floor_number = flat_number % 4 + 1
        print ("flat number is: ", flat_number, "floor number is: ", floor_number, "entrance number is: ", entrance_number)
    elif flat_number == 0:
        break
    else:
        print ("invalid flat number")
