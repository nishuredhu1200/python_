# simple calculator(choose option and operation on two numbers)

a = int(input("enter first number:"))
b = int(input("enter second number:"))

print("1 for addition / 2 for subtraction / 3 for multiplication / 4 for division ")
choicee= int(input(" enter your choice"))
A= a+b
S= a-b
M=a*b
D= a//b

if choicee==1 :
    print(A," addition of two nunbers")
elif choicee==2:
    print(S," subtration of two numbers")
elif choicee==3:
    print(M," multiplicatin of two numbers")
elif choicee==4:
    print(D," floor division of two numbers")
else :
    print(" error!!!!")    

