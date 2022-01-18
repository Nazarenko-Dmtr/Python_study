# task 5

number = int(input("enter any 3 digit number: "))

sum_of_digits = number // 100 + number % 100 // 10 + number % 10
  
print ("sum_of_digits =", sum_of_digits)

