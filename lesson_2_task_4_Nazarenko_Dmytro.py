# task 4

number_of_card = int (input("Enter 16-th digit card number: "))
while True:
   if number_of_card > 10 ** 15 and number_of_card < 10 ** 16:
         print (number_of_card % 10 ** 4)
         number_of_card = int (input("Enter 16-th digit card number: "))
   elif number_of_card == 0:
         break
   else: 
         print ("only 16-th number acceptable")
         number_of_card = int (input("Enter 16-th digit card number: "))
