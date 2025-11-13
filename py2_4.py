# write a loop that prints all elements that appearmore than once in a list
my_list=[1,6,8,6,7,90,89,7,90,4,5,4,8]
duplicates=[] # empty list to store duplicates 
# loop througgh the list 
for item in my_list:
    if my_list.count(item)>1 and item not in duplicates: 
        duplicates.append(item)
        # to print duplicates items
print(" elements appearing more than once:" , duplicates)