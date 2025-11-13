#take a number as input and print its multiplication table using a loop
num=int(input(" enter the number"))
for i in range(1 , 11) :
    print(num ,'x', i, ' =', num *i , end="  ")