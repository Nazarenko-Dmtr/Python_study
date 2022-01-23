
# Lesson 4, Task 2, Variant 2

while True:
    number = int(input("Enter any number: "))
    if number == 0:
        break
    else:
        my_list = list(str(number))
        reversed_list = my_list[::-1]
        print(my_list == reversed_list)
