# task 7 + 8

number = int(input("enter any number: "))

sum_of_figures = 0
figures_quantity = 0

while number > 0:
    figures_quantity += 1 
    sum_of_figures += number % 10
    number = number // 10
    
print (figures_quantity, sum_of_figures, sep = ",")
