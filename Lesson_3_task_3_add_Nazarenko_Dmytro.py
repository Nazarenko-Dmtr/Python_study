# task add # 3

side_a = int(input("insert length of side a: "))
side_b = int(input("insert length of side b: "))   
side_c = int(input("insert length of side c: "))    
if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
    print ("such triangle exist")
else: 
    print ("such triangle does not exist")
