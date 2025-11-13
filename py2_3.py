# loop through a dictionary and print each key-value pair , and store it in a list.
my_dict= {
    'name' : 'nishu' , 'age' : 20 , 'city' : 'jind'
}
result=[]
for key , value in my_dict.items():
    print(key,":",value)
    result.append((key , value))
print(" \n list of key-value pairs:", result)