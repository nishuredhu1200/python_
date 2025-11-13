#count even and odd number in a range  input two numbers start and end . print how many even and odd number exist b/w them.
#(inclusive)
start=int(input(" enter starting number :"))
end = int(input(" enter ending number :"))
even = 0
odd = 0
for i in range(start , end+1):
    if i %2== 0:
        
        even = even +1
        print(i)
    
    else :
    
        odd = odd +1
        
print(" total even numbers",even)
print(" total odd numbers :" ,odd)