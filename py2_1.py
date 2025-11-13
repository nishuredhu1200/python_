#use loops logic and check the number is palidrome or not
num=int(input(" enter a  number "))
temp= num 
rev = 0
while temp>0:
    Digit = temp % 10
    rev= rev *10 + Digit
    temp=temp//10
if num==rev:
    print(" true palindrome")
else:
    print(" false")