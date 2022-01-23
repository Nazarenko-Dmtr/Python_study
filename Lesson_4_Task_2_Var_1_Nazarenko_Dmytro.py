# Lesson 4, Task 2, Variant 1

while True:
    number = int(input("Enter any number: "))
    if number == 0:
        break

    else:
        my_list = list(str(number))

        new_list = my_list[:]
        length = len(my_list)

        for i in range(length // 2):
            my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

        print(my_list == new_list)
