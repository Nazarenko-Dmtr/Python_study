# Lesson 4, Task 1

while True:
    number = int (input("Enter any number: "))
    my_list = list(map(int, str(number)))
    reversed_list = my_list [::-1]
    if number == 0:
        break
    elif len(my_list) % 2 == 1:
        print ("enter number with even quantity of figures: ")
    else:
        length = int (len (my_list)/2)
        new_list_1 = []
        new_list_2 = []
        for i in range (length):
            new_list_1.append(my_list [i])
            new_list_2.append(reversed_list [i])
        print ("Sum of the first half of number is: ", sum(new_list_1), "\nSum of the second half of number is: ", sum(new_list_2), "\n", (sum(new_list_1))==(sum(new_list_2)), sep = "")
