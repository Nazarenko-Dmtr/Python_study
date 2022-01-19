# task # 5

largest_number = - 10**1000
counter = 0

while counter < 3:
    number = int(input("Enter number: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number
print("The largest number is", largest_number)
